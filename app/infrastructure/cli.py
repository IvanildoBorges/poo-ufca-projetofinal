from app.domain.models.Livro import Livro
from app.domain.models.Revista import Revista
from app.domain.enums.status_leitura import StatusLeitura
from app.services.relatorios import Relatorio

class CLIInterface:
    def __init__(self, colecao, repositorio, configuracoes):
        self.colecao = colecao
        self.repositorio = repositorio
        self.configuracoes = configuracoes

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()

            match opcao:
                case "1":
                    self.handle_cadastrar()
                case "2":
                    self.handle_listar()
                case "3":
                    self.handle_relatorios()
                case "4":
                    self.handle_salvar()
                case "5":
                    self.handle_carregar()
                case "6":
                    self.handle_status_leitura()
                case "7":
                    self.handle_avaliar()
                case "0":
                    print("Encerrando o sistema...")
                    break
                case _:
                    print("Opção inválida!")


    def mostrar_menu(self):
        print("\n📚 Biblioteca Digital Pessoal")
        print("1 - Cadastrar publicação")
        print("2 - Listar publicações")
        print("3 - Relatórios")
        print("4 - Salvar dados")
        print("5 - Carregar dados")
        print("6 - Alterar status de leitura")
        print("7 - Avaliar publicação")
        print("0 - Sair")

    def selecionar_publicacao(self):
        if not self.colecao.publicacoes:
            print("Nenhuma publicação cadastrada!")
            return None

        for i, pub in enumerate(self.colecao.publicacoes):
            print(f"{i + 1} - {pub} [{pub.status.value}]")

        try:
            indice = int(input("Escolha a publicação: ")) - 1
            return self.colecao.publicacoes[indice]
        except (ValueError, IndexError):
            print("Seleção inválida!")
            return None

    def handle_cadastrar(self):
        print("\nCadastrar:")
        print("1 - Livro")
        print("2 - Revista")
        tipo = input("Escolha uma opções numéricas anteriores: ")

        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        if tipo == "1":
            isbn = input("ISBN: ")
            livro = Livro(titulo, autor, ano, isbn) # pyright: ignore
            self.colecao.adicionar_publicacao(livro)
            print("📘 Livro cadastrado com sucesso!")

        elif tipo == "2":
            edicao = input("Edição: ")
            periodicidade = input("Periodicidade: ")
            revista = Revista(titulo, autor, ano, edicao = edicao, periodicidade = periodicidade) # pyright: ignore
            self.colecao.adicionar_publicacao(revista)
            print("📗 Revista cadastrada com sucesso!")

        else:
            print("Tipo inválido!")

    def handle_listar(self):
        print("\n📄 Publicações:")
        if len(self.colecao.publicacoes) == 0:
                print("Nenhuma publicação encontrada!")
        else:
            for pub in self.colecao.publicacoes:
                print(pub)

    def handle_relatorios(self):
        relatorio = Relatorio(self.colecao)
        print("\n📊 Relatórios")
        print("1 - Média de avaliações")
        print("2 - Verificar meta anual")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Média:", relatorio.media_avaliacoes_lidas())
        elif opcao == "2":
            meta = self.configuracoes.obter_meta_anual()
            print(f"Sua meta é de {meta} leituras por ano.")

    def handle_salvar(self):
        self.repositorio.salvar(self.colecao)
        print("💾 Dados salvos com sucesso!")

    def handle_carregar(self):
        self.colecao.publicacoes = self.repositorio.carregar()
        print("📂 Dados carregados com sucesso!")

    def handle_status_leitura(self):
        print("\n📖 Alterar status de leitura")
        pub = self.selecionar_publicacao()
        if not pub:
            return
        print("1 - Iniciar leitura")
        print("2 - Concluir leitura")
        opcao = input("Escolha: ")
        try:
            if opcao == "1":
                pub.iniciar_leitura()
                print("Leitura iniciada!")
            elif opcao == "2":
                pub.concluir_leitura()
                print("Leitura concluída!")
            else:
                print("Opção inválida!")
        except ValueError as e:
            print(f"Erro: {e}")

    def handle_avaliar(self):
        print("\n⭐ Avaliar publicação")
        pub = self.selecionar_publicacao()
        if not pub:
            return
        try:
            nota = float(input("Nota (0 a 5): "))
            pub.avaliacao = nota
            print("Avaliação registrada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")
