from datetime import datetime
from factory.compromisso_factory import CompromissoFactory


def adicionar_compromisso():
    """
    Cria um novo compromisso com base nos dados inseridos pelo usuário.

    Retorna:
    - Compromisso: objeto criado, caso válido.
    - None: se a criação for cancelada ou inválida.
    """
    return CompromissoFactory.criar()


def listar_compromissos(compromissos, ordem):
    """
    Exibe a lista de compromissos com ordenação opcional.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação ('1' = data/hora, '2' = nome).
    """
    if not compromissos:
        print("Nenhum compromisso registrado...")
        return

    if ordem == '1':
        compromissos_ordenados = sorted(compromissos, key=lambda c: datetime.combine(c.data, c.hora))
    elif ordem == '2':
        compromissos_ordenados = sorted(compromissos, key=lambda c: c.nome)
    else:
        compromissos_ordenados = compromissos

    for i, comp in enumerate(compromissos_ordenados, start=1):
        print(f"{i} - {comp}")

def remover_compromisso(compromissos, ordem):
    """
    Remove um compromisso da lista com base na posição selecionada pelo usuário.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').
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

def alterar_compromisso(compromissos, ordem):
    """
    Permite alterar os dados de um compromisso selecionado.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').
    """    
    if not compromissos:
        print("Nenhum compromisso registrado...")
        return
    
    listar_compromissos(compromissos, ordem)
    try:
        escolha = int(input("Digite o número do compromisso que deseja alterar:"))
        if not(1 <= escolha <= len(compromissos)):
            print(f"Não existe compromisso com o índice {escolha}")
            return

        CompromissoFactory.editar(compromissos[escolha - 1])
        print(f"Compromisso alterado com sucesso:\n")
    except ValueError:
        print("Favor informar um número válido")
        
def concluir_compromisso(compromissos, ordem):
    """
    Marca um compromisso como concluído.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').
    """
    if not compromissos:
        print("Nenhum compromisso registrado...")
        return

    listar_compromissos(compromissos, ordem)
    try:
        escolha = int(input("Digite o número do compromisso que deseja marcar como concluído:"))
        if not (1 <= escolha <= len(compromissos)):
            print(f"Não existe compromisso com o índice {escolha}")
            return

        CompromissoFactory.concluir(compromissos[escolha - 1])
    except ValueError:
        print("Favor informar um número válido")