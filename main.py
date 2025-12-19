from app.domain.models.Colecao import Colecao
from app.infrastructure.repositorio import JSONRepositorio
from app.infrastructure.configuracoes import Configuracoes
from app.infrastructure.cli import CLIInterface

def main():
    colecao = Colecao()
    repositorio = JSONRepositorio("app/utils/data.json")
    configuracoes = Configuracoes("app/utils/config.json")

    cli = CLIInterface(colecao, repositorio, configuracoes)
    cli.iniciar()

if __name__ == "__main__":
    main()
