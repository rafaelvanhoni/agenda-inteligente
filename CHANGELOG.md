# Changelog

Todas as alterações notáveis neste projeto serão documentadas aqui, seguindo o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

## [v0.9.5] - 2025-07-02

### Alterado
- Refatoração completa da lógica de negócio:
  - Criação do módulo `compromisso_service.py` com as funções `criar_compromisso`, `editar_compromisso` e `concluir_compromisso`.
  - Transferência da lógica de validação e input de dados da factory para o service.
  - Controller atualizado para utilizar diretamente os métodos do service.
- `CompromissoFactory` agora atua apenas como instanciador de objetos, conforme o princípio da responsabilidade única (SRP).

### Estrutura
- Pasta `factory/` renomeada para `factories/`, seguindo o padrão de nomenclatura no plural adotado nas demais camadas.
- Imports atualizados para refletir a nova estrutura.

### Corrigido
- Corrigido erro de chamada aos métodos `editar()` e `concluir()` que ainda estavam referenciando a factory após a refatoração.

## [v0.9.4] - 2025-07-01

### Adicionado
- Função `ordenar_compromissos()` no módulo `agenda_services`, permitindo ordenação por data/hora ou nome.
- Função `verificar_compromissos()` no `agenda_controller`, com verificação centralizada da lista de compromissos.
- Docstrings explicativas adicionadas às funções `ordenar_compromissos()` e `verificar_compromissos()`.
- Docstrings padronizadas com uso de hífens (`-`) em todos os métodos do projeto.

### Alterado
- Refatoração das funções `listar_compromissos()`, `remover_compromisso()`, `alterar_compromisso()`, `concluir_compromisso()` e `selecionar_compromisso()` para utilizar `verificar_compromissos()`, eliminando duplicações.
- Padronização do tipo de retorno `-> Compromisso | None` em todos os métodos relevantes.
- Retorno explícito de `None` adicionado em funções com saídas condicionais, promovendo consistência.
- Melhoria geral na coesão e legibilidade do código.

### Corrigido
- Ajustes nas mensagens de erro e validação para manter uniformidade e clareza no terminal.

## [v0.9.3] - 2025-06-11

### Adicionado
- Método `__str__()` completo na classe `Compromisso`, exibindo todos os campos com formatação legível, incluindo data e hora de conclusão.
- Método `resumo()` na classe `Compromisso`, com exibição compacta e formatada para listagens.
- `docstrings` detalhadas para todos os métodos da classe `Compromisso`.
- Inclusão da opção **5 – Concluir compromisso** no menu principal (`main.py`), chamando a função de conclusão implementada no controller.

### Alterado
- Melhoria na forma de exibição do `resumo()`, limitando o nome a 20 caracteres e exibindo campos booleanos como "Sim"/"Não".
- Atualização nos testes automatizados do módulo `validador.py` com cobertura completa para `validar_data`, `validar_hora`, `validar_data_hora`, `validar_bool`, `validar_obrigatorio` e `validar_tamanho`.

### Corrigido
- Correção na exibição dos campos de data e hora de conclusão no método `__str__()`, que antes estavam ausentes ou com valores incorretos.
- Correção na chamada incorreta do campo `self.importante` no `resumo()` (duplicado no lugar de `concluido`).

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