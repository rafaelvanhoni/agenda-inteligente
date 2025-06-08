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
    resposta = resposta.strip().lower()
    if resposta in ['sim', 's', '1', 'true', 't']:
        return True
    elif resposta in ['não', 'nao', '0', 'false', 'f']:
        return False
    else:
        print("Entrada inválida. Informe 'sim' ou 'não'")
        return None

def validar_obrigatorio(campo: str, nome_campo: str) -> str | None:
    campo = campo.strip()
    if not campo:
        print(f"'{nome_campo}' não pode ser em branco.")
        return None
    return campo

def validar_tamanho(campo: str, nome_campo: str, limite: int) -> bool:
    if len(campo) > limite:
        print(f"'{nome_campo}' tem um tamanho máximo de {limite} caracteres.")
        return False
    return True