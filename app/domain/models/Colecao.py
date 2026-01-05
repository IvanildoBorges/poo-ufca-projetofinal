from app.domain.models.Publicacao import Publicacao

class Colecao:
    def __init__(self):
        self.publicacoes = []

    def adicionar_publicacao(self, publicacao: Publicacao):
      # Verifica se a publicacão já existe na colecão e adiciona uma nova publicacão à colecão caso ela não exista
      if publicacao in self.publicacoes:
          raise ValueError("Publicação já existe na coleção")
      self.publicacoes.append(publicacao)

    def listar_publicacoes(self):
      return self.publicacoes

    def __len__(self):
        return len(self.publicacoes)

    def __iter__(self):
        # Tornar a classe Colecao iterável
        return iter(self.publicacoes)
