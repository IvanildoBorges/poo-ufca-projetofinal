from abc import ABC, abstractmethod
from datetime import datetime
from app.domain.enums.status_leitura import StatusLeitura

class Publicacao(ABC):
    def __init__(self, titulo: str, autor: str, ano: int, genero: str, num_paginas: int):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._genero = genero
        self._num_paginas = num_paginas
        self._status = StatusLeitura.NAO_LIDO
        self._avaliacao = None
        self._data_inclusao = datetime.now()
        self._data_inicio_leitura = None
        self._data_fim_leitura = None
        self._anotacoes = []
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value or not value.strip():
            raise ValueError("Título não pode ser vazio")
        self._titulo = value
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, value):
        if value < 1500:
            raise ValueError("Ano deve ser maior ou igual a 1500")
        self._ano = value
    
    @property
    def avaliacao(self):
        return self._avaliacao
    
    @property
    def status(self):
        return self._status

    @avaliacao.setter
    def avaliacao(self, value):
        if self._status != StatusLeitura.LIDO:
            raise ValueError("Avaliação só pode ser feita após concluir a leitura")
        if not 0 <= value <= 10:
            raise ValueError("Avaliação deve estar entre 0 e 10")
        self._avaliacao = value
    
    def iniciar_leitura(self):
        if self._status == StatusLeitura.NAO_LIDO:
            self._status = StatusLeitura.LENDO
            self._data_inicio_leitura = datetime.now()
    
    def concluir_leitura(self):
        if self._status == StatusLeitura.LENDO and self._data_inicio_leitura:
            self._status = StatusLeitura.LIDO
            self._data_fim_leitura = datetime.now()
        else:
            raise ValueError("Não é possível marcar como LIDO sem data de início")
    
    def __str__(self):
        return f"{self._titulo} - {self._autor} ({self._ano})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(titulo='{self._titulo}', autor='{self._autor}', ano={self._ano}, status={self._status.value})"
    
    def __lt__(self, other):
        if not isinstance(other, Publicacao):
            return NotImplemented
        return self._ano < other._ano
    
    def __eq__(self, other):
        return self._titulo == other._titulo and self._autor == other._autor
    
    @abstractmethod
    def tipo(self):
        pass