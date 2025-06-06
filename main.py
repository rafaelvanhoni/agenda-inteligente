import agenda
from utils import limpar_tela

def mostrar_menu():
    print("===== AGENDA INTELIGENTE =====")
    print("1 - Adicionar compromisso")
    print("2 - Listar compromissos")
    print("3 - Remover compromissos")
    print("0 - Sair")

compromissos = []

if __name__ == "__main__":
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(">>> Adicionando compromisso")

            compromisso = agenda.adicionar_compromisso()
            if compromisso != None:
                compromissos.append(compromisso)
        elif opcao == "2":
            print(">>> Listando compromissos")
            print("Para Ordenar, digite:")
            print("1 - Por Data")
            print("2 - Por Nome")
            print("Qualquer outra tecla, mantem a ordem padrão...")
            opcao_ordenacao = input("Escolha uma opção: ")
            agenda.listar_compromissos(compromissos, opcao_ordenacao)
        elif opcao == "3":
            agenda.remover_compromisso(compromissos)
        elif opcao == "0":
            print(">>> Encerrando programa")
            break
        else:
            print(">>> Opção inválida. Tente novamente.")

        input("\nPressione qualquer tecla para continuar...")


       