from app.domain.enums.status_leitura import StatusLeitura
from app.domain.models.Publicacao import Publicacao
from app.domain.models.Colecao import Colecao

class Relatorio:
    def __init__(self, colecao: Colecao):
        self.colecao = colecao

    def total_publicacoes(self):
        """Retorna o número total de publicações na coleção."""
        return len(self.colecao)

    def status_leitura_resumo(self):
        """Calcula a quantidade e o percentual de publicações por status de leitura."""
        total_de_publicacoes = self.total_publicacoes()

        if total_de_publicacoes == 0:
            return {status.value: {"quantidade": 0, "percentual": 0.0} for status in StatusLeitura}

        contagem_status = {
            StatusLeitura.NAO_LIDO: 0,
            StatusLeitura.LENDO: 0,
            StatusLeitura.LIDO: 0
        }

        for publicacao in self.colecao:
            contagem_status[publicacao.status] += 1

        # Prepara o dicionário de resultados para o relatório
        resumo_status = {}
        for status_enum, quantidade in contagem_status.items():
            # Calcula o percentual para cada status
            percentual = (quantidade / total_de_publicacoes) * 100
            # Adiciona os dados ao dicionário de resumo, usando o nome do status
            resumo_status[status_enum.value] = {"quantidade": quantidade, "percentual": percentual}

        return resumo_status

    def media_avaliacoes_lidas(self):
        """Calcula a média das avaliações das publicações lidas."""
        avaliacoes_validas = []

        for publicacao in self.colecao:
            if publicacao.status == StatusLeitura.LIDO and publicacao.avaliacao is not None:
                avaliacoes_validas.append(publicacao.avaliacao)

        if not avaliacoes_validas:
            return 0.0

        soma_das_avaliacoes = sum(avaliacoes_validas)
        quantidade_de_avaliacoes = len(avaliacoes_validas)
        media = soma_das_avaliacoes / quantidade_de_avaliacoes

        return media

    def top5_avaliadas(self):
        """Retorna as top 5 publicações mais bem avaliadas."""
        publicacoes_avaliadas_e_lidas = []

        for publicacao in self.colecao:
            if publicacao.status == StatusLeitura.LIDO and publicacao.avaliacao is not None:
                publicacoes_avaliadas_e_lidas.append(publicacao)

        if not publicacoes_avaliadas_e_lidas:
            return []

        # Ordena a lista de publicações avaliadas: primeiro por avaliação (decrescente)
        # e depois por título (crescente) para desempate.
        publicacoes_avaliadas_e_lidas.sort(key=lambda pub: (-pub.avaliacao, pub.titulo))

        # Retorna apenas as 5 primeiras publicações da lista ordenada (o top 5)
        return publicacoes_avaliadas_e_lidas[:5]

    def gerar_relatorio(self):
        """Gera e imprime um relatório completo da coleção de forma detalhada."""
        print("--- Relatório Detalhado da Coleção de Publicações ---")

        # Informa o total de publicações cadastradas
        total = self.total_publicacoes()
        print(f"Total de publicações cadastradas: {total}")

        # Informa o resumo de status de leitura
        status_resumo = self.status_leitura_resumo()
        print("\n--- Resumo por Status de Leitura ---")
        for nome_status, dados_status in status_resumo.items():
            print(f"- {nome_status}: {dados_status['quantidade']} publicações ({dados_status['percentual']:.2f}%)")

        # Informa a média das avaliações das publicações lidas
        media_avaliacoes = self.media_avaliacoes_lidas()
        if media_avaliacoes > 0:
            print(f"\n--- Média das Avaliações (publicações lidas): {media_avaliacoes:.2f} ---")
        else:
            print("\n--- Nenhuma publicação lida e avaliada para calcular a média. ---")
