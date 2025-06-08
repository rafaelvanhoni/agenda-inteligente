from datetime import datetime

def validar_data_hora(data_hora):
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



