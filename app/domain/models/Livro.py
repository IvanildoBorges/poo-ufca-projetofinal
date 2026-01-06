from app.domain.models.Publicacao import Publicacao

class Livro(Publicacao):
    def __init__(
            self, 
            titulo: str, 
            autor: str, 
            ano: int, 
            isbn: str, 
            genero: str = "Desconhecido", 
            num_paginas: int = 0
        ):
        super().__init__(titulo, autor, ano, genero, num_paginas)
        self.isbn = isbn
    
    def tipo(self):
        return "Livro"
    
    def __str__(self):
        return f"Livro: {self.titulo} - {self.autor} ({self.ano}) ISBN: {self.isbn}"