import os

def limpar_tela():
    """
    Limpa o terminal no Windows ou Linux/MacOS
    """
    os.system('cls' if os.name == 'nt' else 'clear')