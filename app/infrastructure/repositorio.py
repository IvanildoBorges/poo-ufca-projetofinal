import json
from abc import ABC, abstractmethod
from typing import List
from app.domain.models.Livro import Livro
from app.domain.models.Revista import Revista
from app.domain.enums.status_leitura import StatusLeitura

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, colecao) -> None:
        pass

    @abstractmethod
    def carregar(self) -> List:
        pass

class JSONRepositorio(Repositorio):
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def salvar(self, colecao):
        dados = {
            "publicacoes": []
        }

        for pub in colecao.publicacoes:
            item = {
                "tipo": pub.__class__.__name__,
                "titulo": pub.titulo,
                "autor": pub.autor,
                "ano": pub.ano,
                "status": pub.status.name,
                "avaliacao": pub.avaliacao
            }

            if isinstance(pub, Livro):
                item["isbn"] = pub.isbn

            elif isinstance(pub, Revista):
                item["edicao"] = pub.edicao
                item["periodicidade"] = pub.periodicidade

            dados["publicacoes"].append(item)

        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar(self):
        publicacoes = []

        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados.get("publicacoes", []):
                status = StatusLeitura[item["status"]]

                if item["tipo"] == "Livro":
                    pub = Livro(
                        item["titulo"],
                        item["autor"],
                        item["ano"],
                        item["isbn"]
                    )

                elif item["tipo"] == "Revista":
                    pub = Revista(
                        item["titulo"],
                        item["autor"],
                        item["ano"],
                        item["edicao"],
                        item["periodicidade"]
                    )
                else:
                    continue

                pub.status = status
                pub.avaliacao = item.get("avaliacao")

                publicacoes.append(pub)

        except FileNotFoundError:
            pass  # arquivo ainda não existe

        return publicacoes
