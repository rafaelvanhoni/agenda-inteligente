# 🧠 Agenda Inteligente (Terminal)

Projeto em Python para gerenciamento de compromissos, desenvolvido com fins educacionais. Permite adicionar, listar (com ordenação) e remover compromissos diretamente pelo terminal.

## 📦 Estrutura do Projeto

```
agenda_inteligente/
├── main.py                # Programa principal com menu de navegação
├── agenda.py              # Funções para adicionar, listar e remover compromissos
├── modelo.py              # Classe Compromisso (orientado a objetos)
├── validador.py           # Validação de data e hora
├── utils.py               # Função utilitária para limpar a tela
├── teste.py               # Arquivo auxiliar para testes manuais
├── .gitignore             # Arquivos e pastas ignoradas pelo Git
└── README.md              # Este arquivo
```

## ⚙️ Funcionalidades

- ✅ Adicionar novos compromissos com data e hora
- ✅ Validar datas digitadas (formato: `dd/mm/yyyy hh:mm`)
- ✅ Listar compromissos ordenados por:
  - Data
  - Nome
  - Ordem de inclusão
- ✅ Remover compromissos por índice (com validação)
- ✅ Organização do código com Orientação a Objetos (`Compromisso`)

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

- [ ] Salvar compromissos em arquivo (persistência)
- [ ] Melhor tratamento de erros
- [ ] Interface gráfica (versão futura)

---

Desenvolvido com 💻 e café por Rafael Vanhoni
