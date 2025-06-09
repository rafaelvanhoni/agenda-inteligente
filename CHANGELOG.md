# Changelog

Todas as alterações notáveis neste projeto serão documentadas aqui, seguindo o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

## [v0.9.1] - 2025-06-09
### Adicionado
- Método `editar()` na `CompromissoFactory` para alteração seletiva de campos com validação.
- Método `concluir()` na `CompromissoFactory`, com suporte à entrada manual ou automática de data/hora.
- Funções `alterar_compromisso()` e `concluir_compromisso()` no `agenda.py`.
- Opção "Concluir compromisso" adicionada ao menu principal no `main.py`.

### Alterado
- Melhorias gerais na organização do fluxo de entrada de dados do usuário.

## [v0.9.0] - 2025-06-08
### Adicionado
- Funcionalidade de adicionar e listar compromissos com ordenação por nome ou data/hora.
- Validações reutilizáveis implementadas no módulo `validador.py`.
- Estrutura do projeto reorganizada com os diretórios `model/`, `factory/`, e `utils/`.
