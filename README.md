# 🧠 Agenda Inteligente (Terminal)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![VS Code](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)

Projeto em Python para gerenciamento de compromissos, desenvolvido com fins educacionais. Permite adicionar, listar (com ordenação), remover, alterar e concluir compromissos diretamente pelo terminal.

## 📦 Estrutura do Projeto

```
agenda_inteligente/
├── app/
│   ├── main.py                          # Programa principal com menu de navegação
│   ├── controllers/
│   │   └── agenda_controller.py         # Funções de controle de compromissos
│   ├── core/
│   │   └── models/
│   │       └── compromisso.py           # Classe Compromisso (entidade principal)
│   ├── factories/
│   │   └── compromisso_factory.py       # Fábrica de Compromissos
│   ├── services/
│   │   └── agenda_services.py           # Função de ordenação dos compromissos
│   ├── utils/
│   │   └── limpar_tela.py               # Função utilitária para limpar a tela
│   └── validators/
│       └── validador.py                 # Funções de validação (datas, textos, booleanos)
├── tests/
│   └── app/
│       └── validators/
│           └── test_validador.py       # Testes automatizados com pytest
├── rascunho/                            # Arquivos auxiliares e experimentações
├── .gitignore                           # Arquivos e pastas ignoradas pelo Git
├── CHANGELOG.md                         # Registro de alterações
└── README.md                            # Este arquivo
```

## ⚙️ Funcionalidades

- ✅ Adicionar novos compromissos com data e hora
- ✅ Validar campos obrigatórios, datas, horas e booleanos
- ✅ Listar compromissos ordenados por:
  - Data e Hora
  - Nome
  - Ordem de inclusão
- ✅ Remover compromissos com confirmação e validação
- ✅ Alterar dados de compromissos já existentes
- ✅ Marcar compromissos como concluídos, com data e hora manual ou automática
- ✅ Representação completa (`__str__`) e resumida (`resumo`) dos compromissos
- ✅ Organização do código com Clean Architecture (camadas separadas)
- ✅ Separação de responsabilidades com uso de `services` para lógica de negócio
- ✅ Refatoração do controller com centralização de validações e uso de funções auxiliares
- ✅ Testes automatizados com `pytest` cobrindo todos os validadores

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/rafaelvanhoni/agenda-inteligente.git
cd agenda-inteligente
```

2. Execute o programa com o módulo principal:

```bash
python -m app.main
```

> **Requisitos**: Python 3.10+ e terminal compatível (Unix/Linux/Mac ou Windows)

## 📝 Observações

- Este projeto está sendo desenvolvido passo a passo como parte dos estudos em Python e boas práticas de arquitetura.
- O código é documentado com `docstrings` e comentários para facilitar o aprendizado e manutenção.
- Testes com `pytest` foram iniciados e continuam sendo expandidos.
- O VS Code está configurado para ocultar arquivos auxiliares como `__init__.py` e `__pycache__` da visualização.

## 📅 Próximas melhorias (to-do)

- [ ] Aumentar a cobertura de testes automatizados (incluindo controller e factory)
- [ ] Persistência de dados (salvar e carregar compromissos com JSON ou banco de dados)
- [ ] Interface gráfica (versão futura com `tkinter`, `PyQt` ou web)

---

Desenvolvido com 💻, ☕ e [VS Code](https://code.visualstudio.com/) por Rafael Vanhoni

> Versão atual: `v0.9.5`