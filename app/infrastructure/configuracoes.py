import json

class Configuracoes:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self._settings = {}
        self.carregar_configuracoes()

    def carregar_configuracoes(self):
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                self._settings = json.load(f)
        except FileNotFoundError:
            self._settings = {
                "meta_anual": 0
            }

    def obter_meta_anual(self) -> int:
        return self._settings.get("meta_anual", 0)
