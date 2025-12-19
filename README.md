# Biblioteca Digital Pessoal
Projeto desenvolvido para gerenciamento de um acervo pessoal de livros e revistas digitais, com foco em Programação Orientada a Objetos (POO), encapsulamento, herança, persistência desacoplada e aplicação de regras de negócio configuráveis.

## Equipe:
| Nome                                    | Responsabilidade              |
| --------------------------------------- | ----------------------------- |
| **CICERO IVANILDO BORGES ALVES**        | *Publicacao, enums, utils, infrastructure e README* |
| **BRENNA ISABELLY DE OLIVEIRA**         | *Revista, Livro e Anotacao* |
| **YAN BRASIL ANGELIM DE BRITO**         | *Colecao, relatorios e mixins* |
| **CICERO DANILO DO NASCIMENTO PEREIRA** | *test_publicacao, test_revista, test_livro, test_anotacao e test_colecao* |

## 1. Arquitetura do Projeto
O projeto segue uma arquitetura baseada em camadas, separando o Domínio (Entidades e Regras) da Infraestrutura (Persistência e Configurações), o que facilita a manutenção e o teste.

**Estrutura de Pastas**
```bash
biblioteca_digital/
├── app/
│   ├──domain/
│   │   ├── models
│   │   │   ├── Publicacao.py
│   │   │   ├── Livro.py
│   │   │   ├── Revista.py
│   │   │   ├── Anotacao.py
│   │   │   └── Colecao.py
│   │   ├── mixins/
│   │   │   └── GerenciamentoLeiturasMixin.py
│   │   └── enums/
│   │       └── status_leitura.py
│   ├── infrastructure/
│   │   ├── repositorio.py          # Repositorio (Interface), JSONRepositorio
│   │   ├── cli.py                  # Interface de Linha de Comando
│   │   └── configuracoes.py
│   └── services/
│   │   └── relatorios.py           # Gerador de Relatorios
│   └── utils/
│       └── data.json               # dados para alimentar o sistema de biblioteca
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## 2. Modelagem Orientada a Objetos (POO)
**2.1. Diagrama de Classes UML (Textual)**
O diagrama abaixo detalha as classes principais, suas relações de herança, e os atributos e métodos essenciais.

**1. Classes de Domínio (Entidades e Herança)**
| Classe                      | Herança / Associação        | Atributos Chave                                     | Métodos Principais                                                  |
| --------------------------- | --------------------------- | --------------------------------------------------- | ------------------------------------------------------------------- |
| **Publicacao** *(Abstrata)* | Base                        | `_titulo`, `_autor`, `_ano`, `status`, `_avaliacao` | `__str__`, `__repr__`, `__lt__`, `__eq__`, `@property` (validações) |
| **Livro**                   | ↑ de `Publicacao`           | `isbn`                                              | `concluir_leitura()`, `iniciar_leitura()`                           |
| **Revista**                 | ↑ de `Publicacao`           | `edicao`, `periodicidade`                           | Herdados                                                            |
| **Anotacao**                | Associação com `Publicacao` | `texto`, `data`, `trecho`                           | `__init__()`                                                        |

**2. Classes de Controle e Estrutura**
| Classe                         | Padrão / Herança   | Atributos Chave                  | Métodos Principais                                                   |
| ------------------------------ | ------------------ | -------------------------------- | -------------------------------------------------------------------- |
| **Colecao**                    | Contém Publicações | `_publicacoes: list[Publicacao]` | `adicionar_publicacao()` (valida duplicidade), `buscar_por_status()` |
| **GerenciamentoLeiturasMixin** | Herança múltipla   | —                                | `validar_limite_simultaneo()`                                        |
| **GeradorRelatorios**          | Serviço            | `colecao`                        | `media_avaliacoes()`, `verificar_meta_anual()`                       |

**3. Classes de Infraestrutura**
| Classe              | Padrão                            | Atributos Chave                           | Métodos Principais                                      |
| ------------------- | --------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| **Repositorio**     | Interface (Strategy / Repository) | —                                         | `salvar()`, `carregar()`                                |
| **JSONRepositorio** | ↓ de `Repositorio`                | `caminho_arquivo`                         | Implementa `salvar()` e `carregar()` em JSON            |
| **Configuracoes**   | Carrega settings                  | `_settings: dict`                         | `obter_meta_anual()`, `carregar_configuracoes()`        |
| **CLIInterface**    | Interface                         | `colecao`, `repositorio`, `configuracoes` | `handle_cadastrar()`, `handle_relatorio()`, `iniciar()` |
