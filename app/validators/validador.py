from datetime import datetime, date, time

def validar_data(data) -> date | None:
    """
    Valida e converte uma string no formato 'dd/mm/yyyy' para um objeto date.
    
    Parâmetros:
    - data (str): string representando data

    Retorna:
    - date se válido, None caso contrário
    """
    try:
        if not data.strip():
            return None
        return datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError as e:
        print(f"Valor inválido: '{e}'.\nUtilize a formatação 'dd/mm/yyyy'")
        return None

def validar_hora(hora) -> time | None:
    """
    Valida e converte uma string no formato 'HH:MM' para um objeto time.
    
    Parâmetros:
    - hora (str): string representando hora

    Retorna:
    - time se válido, None caso contrário
    """
    try:
        if not hora.strip():
            return None
        return datetime.strptime(hora, "%H:%M").time()
    except ValueError as e:
        print(f"Valor inválido: '{e}'.\nUtilize a formatação 'hh:mm'")
        return None

def validar_data_hora(data_hora) -> datetime | None:
    """
    Valida e converte uma string no formato 'dd/mm/yyyy HH:MM' para um objeto datetime.
    
    Parâmetros:
    - data_hora (str): string representando data e hora

    Retorna:
    - datetime se válido, None caso contrário
    """
    try:
        return datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError as e:
        print(f"Valor inválido: '{e}'.\nUtilize a formatação 'dd/mm/yyyy hh:mm'")
        return None

def validar_bool(resposta: str) -> bool | None:
    """
    Converte uma resposta textual para um valor booleano.

    Aceita como verdadeiro: 'sim', 's', '1', 'true', 't'  
    Aceita como falso: 'não', 'nao', 'n', '0', 'false', 'f'

    Parâmetros:
    - resposta (str): entrada textual do usuário

    Retorna:
    - True ou False se for uma entrada válida
    - None se a entrada for inválida
    """    
    resposta = resposta.strip().lower()
    if resposta in ['sim', 's', '1', 'true', 't']:
        return True
    elif resposta in ['não', 'nao', 'n', '0', 'false', 'f']:
        return False
    else:
        print("Entrada inválida. Informe 'sim' ou 'não'")
        return None

def validar_obrigatorio(campo: str, nome_campo: str) -> str | None:
    """
    Verifica se um campo obrigatório foi preenchido.

    Parâmetros:
    - campo (str): valor a ser verificado
    - nome_campo (str): nome do campo (para mensagem de erro)

    Retorna:
    - O próprio campo, se válido
    - None se estiver vazio
    """    
    campo = campo.strip()
    if not campo:
        print(f"'{nome_campo}' não pode ser em branco.")
        return None
    return campo

def validar_tamanho(campo: str, nome_campo: str, limite: int) -> bool:
    """
    Verifica se o valor de um campo não ultrapassa o limite de caracteres.

    Parâmetros:
    - campo (str): valor a ser verificado
    - nome_campo (str): nome do campo (para mensagem de erro)
    - limite (int): número máximo de caracteres permitidos

    Retorna:
    - True se o tamanho for válido
    - False se exceder o limite
    """    
    if len(campo) > limite:
        print(f"'{nome_campo}' tem um tamanho máximo de {limite} caracteres.")
        return False
    return True