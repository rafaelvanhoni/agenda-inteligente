import validador
from modelo import Compromisso


def adicionar_compromisso():
    print("adicionando compromisso")

    nome = input("Nome do compromisso: ")
    data = input("Data e Hora: ")

    data_convertida = validador.validar_data_hora(data)

    if data_convertida == None:
        return None
    
    return Compromisso(nome, data_convertida)    


def listar_compromissos(compromissos, ordem):
    print("listando compromissos")

    if not compromissos:
        print("Nenhum compromisso registrado...")
        return

    if ordem == '1':
        compromissos_ordenados = sorted(compromissos, key=lambda compromisso : compromisso.data )
    elif ordem == '2':
        compromissos_ordenados = sorted(compromissos, key=lambda compromisso : compromisso.nome )
    else:
        compromissos_ordenados = compromissos

    for i, comp in enumerate(compromissos_ordenados, start=1):
        print(f"{i} - {comp}")

def remover_compromisso(compromissos):
    print("removendo compromisso")

    if not compromissos:
        print("Nenhum compromisso registrado...")
        return
    
    listar_compromissos(compromissos, '1')
    try:
        escolha = int(input("Digite o número do compromisso que deseja remover:"))
        if not(1 <= escolha <= len(compromissos)):
            print(f"Não existe compromisso com o índice {escolha}")
            return

        removido = compromissos.pop(escolha - 1)
        print(f"Compromisso removido: {removido}")
    except ValueError:
        print("Favor informar um número válido")