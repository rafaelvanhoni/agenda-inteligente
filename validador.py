from datetime import datetime

def validar_data_hora(data_hora):

    try:
        return datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
    except ValueError as e:
        print(f"Valor inválido: '{e}'.\nUtilize a formatação 'dd/mm/yyyy hh:mm'")
        return None



