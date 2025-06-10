# Changelog

Todas as alterações notáveis neste projeto serão documentadas aqui, seguindo o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

## [v0.9.2] - 2025-06-10

### Adicionado
- Estrutura profissional baseada em Clean Architecture, com separação em `controllers`, `services`, `factories`, `validators`, `utils`, e `core/models`.
- Testes automatizados para as funções `validar_data` e `validar_hora`, cobrindo casos válidos, inválidos e campos em branco.
- Pasta `rascunho/` para experimentações livres fora do código principal.
- Configuração no VS Code para ocultar arquivos `__pycache__` e `__init__.py`, reduzindo a poluição visual da árvore do projeto.

### Alterado
- Validação de campos booleanos atualizada: `validar_bool()` agora aceita `'n'` como resposta falsa e trata corretamente campos em branco.
- `validar_data()` e `validar_hora()` agora retornam `None` ao receberem entradas em branco, evitando exceções em campos opcionais.
- Ajustes gerais em imports para refletir o novo layout de pacotes.

### Corrigido
- Corrigido erro onde a data e hora de conclusão eram solicitadas mesmo quando o compromisso não estava marcado como concluído.
- Corrigida a resposta inválida ao digitar `'n'` como resposta para campos booleanos.

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
