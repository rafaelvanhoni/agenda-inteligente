# 🧠 Agenda Inteligente (Terminal)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![VS Code](https://img.shields.io/badge/Editor-VSCode-blue?logo=visualstudiocode)

Projeto em Python para gerenciamento de compromissos, desenvolvido com fins educacionais. Permite adicionar, listar (com ordenação) e remover compromissos diretamente pelo terminal.

## 📦 Estrutura do Projeto

```
agenda_inteligente/
├── main.py                     # Programa principal com menu de navegação
├── agenda.py                   # Funções para adicionar, listar e remover compromissos
├── factory/                    # Camada de criação de objetos
│   └── compromisso_factory.py  # Fábrica de Compromissos
├── model/                      # Modelos de dados (OOP)
│   └── compromisso.py          # Classe Compromisso (entidade principal)
├── validador.py                # Funções de validação (datas, textos, booleanos)
├── utils.py                    # Função utilitária para limpar a tela
├── teste.py                    # Arquivo auxiliar para testes manuais
├── .gitignore                  # Arquivos e pastas ignoradas pelo Git
└── README.md                   # Este arquivo
```

## ⚙️ Funcionalidades

- ✅ Adicionar novos compromissos com data e hora
- ✅ Validar campos obrigatórios, datas e horas
- ✅ Listar compromissos ordenados por:
  - Data e Hora
  - Nome
  - Ordem de inclusão
- ✅ Remover compromissos com confirmação e validação
- ✅ Organização do código com Orientação a Objetos e camada de fábrica

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/rafaelvanhoni/agenda-inteligente.git
cd agenda-inteligente
```

2. Execute o programa:

```bash
python main.py
```

> **Requisitos**: Python 3.10+ instalado no seu sistema

## 📝 Observações

- Este projeto está sendo desenvolvido passo a passo como parte dos estudos em Python.
- O código é comentado para facilitar o aprendizado e futuras melhorias.
- Sinta-se à vontade para dar sugestões, abrir issues ou fazer um fork!

## 📅 Próximas melhorias (to-do)

- [ ] Alterar compromissos existentes
- [ ] Marcar como concluído com data e hora manual ou automática
- [ ] Persistência de dados (salvar e carregar compromissos)
- [ ] Testes automatizados (com `unittest` ou `pytest`)
- [ ] Interface gráfica (versão futura)

---

Desenvolvido com 💻, ☕ e [VS Code](https://code.visualstudio.com/) por Rafael Vanhoni
