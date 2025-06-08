import agenda
from utils import limpar_tela

def mostrar_menu():
    """
    Exibe o menu principal da Agenda Inteligente.
    """    
    print("===== AGENDA INTELIGENTE =====\n")
    print("1 - Adicionar compromisso")
    print("2 - Listar compromissos")
    print("3 - Remover compromissos")
    print("0 - Sair\n")
    print()

compromissos = []
ordenacao_compromissos = '1' # '1' representa ordenação por data

if __name__ == "__main__":
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n>>> Adicionando compromisso\n")

            compromisso = agenda.adicionar_compromisso()
            if compromisso is not None:
                compromissos.append(compromisso)
        elif opcao == "2":
            print("\n>>> Listando compromissos\n")
            print("Para Ordenar, digite:")
            print("1 - Por Data")
            print("2 - Por Nome")
            print("Qualquer outra tecla, mantém a ordem padrão...\n")
            ordenacao_compromissos = input("Escolha uma opção: ")
            agenda.listar_compromissos(compromissos, ordenacao_compromissos)
        elif opcao == "3":
            agenda.remover_compromisso(compromissos, ordenacao_compromissos)
        elif opcao == "0":
            print("\n>>> Encerrando programa\n")
            break
        else:
            print("\n>>> Opção inválida. Tente novamente.\n")

        input("\nPressione qualquer tecla para continuar...")


       