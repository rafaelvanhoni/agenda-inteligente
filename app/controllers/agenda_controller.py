from app.factory.compromisso_factory import CompromissoFactory
from app.services.agenda_services import ordenar_compromissos
from app.core.models.compromisso import Compromisso

def adicionar_compromisso() -> Compromisso | None:
    """
    Cria um novo compromisso com base nos dados inseridos pelo usuário.

    Retorna:
    - Compromisso: objeto criado, caso válido.
    - None: se a criação for cancelada ou inválida.
    """    
    return CompromissoFactory.criar()


def listar_compromissos(compromissos, ordem) -> None:
    """
    Exibe a lista de compromissos com ordenação opcional.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação ('1' = data/hora, '2' = nome).

    Retorna:
    - None
    """
    if not verificar_compromissos(compromissos):
        return None
    
    compromissos_ordenados = ordenar_compromissos(compromissos, ordem)
    for i, c in enumerate(compromissos_ordenados, start=1):
        print(f"{i} - {c.resumo()}")
    
def remover_compromisso(compromissos, ordem) -> Compromisso | None:
    """
    Remove um compromisso da lista com base na posição selecionada pelo usuário.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').

    Retorna:
    - Compromisso removido, se encontrado.
    - None, caso a lista esteja vazia ou a seleção seja inválida.
    """
    if not verificar_compromissos(compromissos):
        return None
    
    compromisso = selecionar_compromisso(compromissos, ordem)
    if compromisso is None:
        return None
    
    compromissos.remove(compromisso)
    print(f"Compromisso removido com sucesso:\n{compromisso}")

def alterar_compromisso(compromissos, ordem) -> Compromisso | None:
    """
    Permite alterar os dados de um compromisso selecionado.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').

    Retorna:
    - Compromisso alterado, se encontrado.
    - None, caso a lista esteja vazia ou a seleção seja inválida.
    """  
    if not verificar_compromissos(compromissos):
        return None
    
    compromisso = selecionar_compromisso(compromissos, ordem)
    if compromisso is None:
        return None
    
    CompromissoFactory.editar(compromisso)
    print(f"Compromisso alterado com sucesso:\n{compromisso}")
    
        
def concluir_compromisso(compromissos, ordem) -> Compromisso | None:
    """
    Marca um compromisso como concluído.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação para exibição ('1' ou '2').

    Retorna:
    - Compromisso concluído, se encontrado.
    - None, caso a lista esteja vazia ou a seleção seja inválida.
    """
    if not verificar_compromissos(compromissos):
        return None

    compromisso = selecionar_compromisso(compromissos, ordem)
    if compromisso is None:
        return None

    CompromissoFactory.concluir(compromisso)    
    print(f"Compromisso concluído com sucesso:\n{compromisso}")

def selecionar_compromisso(compromissos, ordem) -> Compromisso | None:
    """
    Exibe a lista de compromissos ordenada e permite ao usuário escolher um deles.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.
    - ordem (str): critério de ordenação ('1' ou '2').

    Retorna:
    - Objeto Compromisso selecionado.
    - None, em caso de lista vazia ou entrada inválida.
    """
    if not verificar_compromissos(compromissos):
        return None
    
    try:
        escolha = int(input("Digite o número do compromisso desejado: "))
        if not(1 <= escolha <= len(compromissos)):
            print(f"Índice inválido. Digite um número entre 1 e {len(compromissos)}")
            return None

        compromissos_ordenados = ordenar_compromissos(compromissos, ordem)
        return compromissos_ordenados[escolha - 1]
    
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        return None
    
def verificar_compromissos(compromissos) -> bool:
    """
    Verifica se a lista de compromissos contém elementos.

    Parâmetros:
    - compromissos (list): lista de objetos Compromisso.

    Retorna:
    - True se houver compromissos na lista.
    - False se a lista estiver vazia (com mensagem exibida).
    """  
    if not compromissos:
        print("Nenhum compromisso registrado...")
        return False
    return True