from app.controllers import agenda_controller as agenda
from app.utils.limpar_tela import limpar_tela
from typing import Callable

# Lista principal onde os compromissos são armazenados em tempo de execução
compromissos = []
# Define a ordenação padrão dos compromissos: '1' para data/hora
ordenacao_compromissos = '1'

def mostrar_menu() -> None:
    """
    Exibe o menu principal da Agenda Inteligente com as opções disponíveis.

    Retorna:
    - None
    """
    print("===== AGENDA INTELIGENTE =====\n")
    print("1 - Adicionar compromisso")
    print("2 - Listar compromissos")
    print("3 - Remover compromisso")
    print("4 - Alterar compromisso")
    print("5 - Concluir compromisso")
    print("6 - Detalhar compromisso")
    print("0 - Sair\n")
    print(f"Total de compromissos: {len(compromissos)}\n")

def escolher_ordenacao() -> str:
    """
    Solicita ao usuário que escolha o critério de ordenação da lista de compromissos.

    Opções:
    - '1' = ordenar por data e hora.
    - '2' = ordenar por nome.
    - Qualquer outra entrada mantém a ordenação atual.

    Retorna:
    - str: valor digitado pelo usuário representando a ordenação escolhida.
    """    
    print("\n>>> Listando compromissos\n")
    print("Para Ordenar, digite:")
    print("1 - Por Data e Hora")
    print("2 - Por Nome")
    print("Qualquer outra tecla, mantém a ordem padrão...\n")
    return input("Escolha uma opção: ")    

def executar_com_visualizacao(funcao: Callable[[list, str], None]) -> None:
    """
    Executa uma função que exige visualização prévia dos compromissos.

    Exibe a lista de compromissos com a ordenação atual. Caso existam registros,
    chama a função recebida com a lista e a ordenação como parâmetros.

    Parâmetros:
    - funcao (Callable[[list, str], None]): função a ser executada, que recebe a lista de compromissos e a ordenação.

    Retorna:
    - None
    """    
    if agenda.listar_compromissos(compromissos, ordenacao_compromissos):
        funcao(compromissos, ordenacao_compromissos)

def adicionar_compromisso() -> None:
    print("\n>>> Adicionando compromisso\n")

    compromisso = agenda.adicionar_compromisso()
    if compromisso is not None:
        compromissos.append(compromisso)    

def listar_compromissos() -> None:
    print("\n>>> Listando compromissos\n")
    global ordenacao_compromissos
    ordenacao_compromissos = escolher_ordenacao()
    agenda.listar_compromissos(compromissos, ordenacao_compromissos)

def remover_compromisso() -> None:
    executar_com_visualizacao(agenda.remover_compromisso)

def alterar_compromisso() -> None:
    print("\n>>> Alterando Compromisso\n")
    executar_com_visualizacao(agenda.alterar_compromisso)

def concluir_compromisso() -> None:
    print("\n>>> Concluindo Compromisso\n")
    executar_com_visualizacao(agenda.concluir_compromisso)

def detalhar_compromisso() -> None:
    print("\n>>> Detalhando Compromisso")
    executar_com_visualizacao(agenda.detalhar_compromisso)

def sair() -> None:
    print("\n>>> Encerrando programa\n")
    exit()

acoes_menu = {
    "1": lambda: adicionar_compromisso(),
    "2": lambda: listar_compromissos(),
    "3": lambda: remover_compromisso(),
    "4": lambda: alterar_compromisso(),
    "5": lambda: concluir_compromisso(),
    "6": lambda: detalhar_compromisso(),
    "0": lambda: sair()
}

if __name__ == "__main__":
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        acao = acoes_menu.get(opcao)
        if acao:
            acao()
        else:
            print("\n>>> Opção inválida. Tente novamente.\n")

        input("\nPressione qualquer tecla para continuar...")
       
