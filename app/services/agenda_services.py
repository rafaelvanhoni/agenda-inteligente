from datetime import datetime

def ordenar_compromissos(compromissos: str, ordem: str) -> list:
    if ordem == '1':
        compromissos_ordenados = sorted(compromissos, key=lambda c: datetime.combine(c.data, c.hora))
    elif ordem == '2':
        compromissos_ordenados = sorted(compromissos, key=lambda c: c.nome)
    else:
        compromissos_ordenados = compromissos
    
    return compromissos