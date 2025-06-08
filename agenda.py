import validador
from modelo import Compromisso


def adicionar_compromisso():
    """
    Cria um novo compromisso a partir dos dados inseridos pelo usuário.

    Retorna:
    - Um objeto Compromisso, se a data for válida.
    - None, caso a data seja inválida.
    """    

    nome = input("Nome do compromisso: ")
    data = input("Data e Hora: ")

    data_convertida = validador.validar_data_hora(data)

    if data_convertida is None:
        return None
    
    return Compromisso(nome, data_convertida)    


def listar_compromissos(compromissos, ordem):
    """
    Exibe a lista de compromissos, com opção de ordenação por nome ou data.

    Parâmetros:
    - compromissos: lista de objetos Compromisso
    - ordem: string indicando a ordenação desejada ('1' para data, '2' para nome).
    """    

    if not compromissos:
        print("Nenhum compromisso registrado...")
        return

    if ordem == '1':
        compromissos_ordenados = sorted(compromissos, key=lambda compromisso: compromisso.data )
    elif ordem == '2':
        compromissos_ordenados = sorted(compromissos, key=lambda compromisso: compromisso.nome )
    else:
        compromissos_ordenados = compromissos

    for i, comp in enumerate(compromissos_ordenados, start=1):
        print(f"{i} - {comp}")

def remover_compromisso(compromissos, ordem):
    """
    Remove um compromisso da lista com base no número selecionado pelo usuário.

    Parâmetros:
    - compromissos: lista de objetos Compromisso.
    - ordem: string com o critério de ordenação para exibição antes da remoção.
    """    

    if not compromissos:
        print("Nenhum compromisso registrado...")
        return
    
    listar_compromissos(compromissos, ordem)
    try:
        escolha = int(input("Digite o número do compromisso que deseja remover:"))
        if not(1 <= escolha <= len(compromissos)):
            print(f"Não existe compromisso com o índice {escolha}")
            return

        removido = compromissos.pop(escolha - 1)
        print(f"Compromisso removido com sucesso:\n{removido}")
    except ValueError:
        print("Favor informar um número válido")