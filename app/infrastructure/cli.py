from app.domain.models.Livro import Livro
from app.domain.models.Revista import Revista
from app.domain.enums.status_leitura import StatusLeitura
#from app.services.relatorios import GeradorRelatorios

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
        print("0 - Sair")

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
            livro = Livro(titulo, autor, ano, isbn)
            self.colecao.adicionar_publicacao(livro)
            print("📘 Livro cadastrado com sucesso!")

        elif tipo == "2":
            edicao = input("Edição: ")
            periodicidade = input("Periodicidade: ")
            revista = Revista(titulo, autor, ano, edicao, periodicidade)
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

    # def handle_relatorios(self):
    #     relatorio = GeradorRelatorios(self.colecao)
    #     print("\n📊 Relatórios")
    #     print("1 - Média de avaliações")
    #     print("2 - Verificar meta anual")
    #     opcao = input("Escolha: ")
    #     if opcao == "1":
    #         print("Média:", relatorio.media_avaliacoes())
    #     elif opcao == "2":
    #         meta = self.configuracoes.obter_meta_anual()
    #         print(relatorio.verificar_meta_anual(meta))

    def handle_salvar(self):
        self.repositorio.salvar(self.colecao)
        print("💾 Dados salvos com sucesso!")

    def handle_carregar(self):
        self.colecao.publicacoes = self.repositorio.carregar()
        print("📂 Dados carregados com sucesso!")
