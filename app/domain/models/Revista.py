from app.domain.models.Publicacao import Publicacao

class Revista(Publicacao):
    def __init__(
            self, 
            titulo: str, 
            autor: str, 
            ano: int, 
            edicao: str, 
            periodicidade: str,
            genero: str = "Desconhecido", 
            num_paginas: int = 0
        ):
        super().__init__(titulo, autor, ano, genero, num_paginas)
        self.edicao = edicao
        self.periodicidade = periodicidade

    def tipo(self):
        return "Revista"
    
    def __str__(self):
        return f"Revista: {self.titulo} - ({self.autor}) {self.ano} Edição: {self.edicao} Periodicidade: {self.periodicidade}"