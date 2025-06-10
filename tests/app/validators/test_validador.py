from datetime import date, time
from app.validators.validador import validar_data, validar_hora

def test_validar_data_valida():
    assert validar_data('01/10/2025') == date(2025, 10, 1)
    assert validar_data('05/12/2024') == date(2024, 12, 5)

def test_validar_data_invalida():
    assert validar_data('32/01/2025') is None
    assert validar_data('15/18/2025') is None

def test_valida_data_em_branco():
    assert validar_data("   ") is None
    assert validar_data("") is None

def test_valida_hora_valida():
    assert validar_hora('12:00') == time(12, 0)
    assert validar_hora('08:30') == time(8, 30)
    assert validar_hora('23:59') == time(23, 59)
    assert validar_hora('00:00') == time(0, 0)

def test_valida_hora_invalida():
    assert validar_hora("27:15") is None
    assert validar_hora("13") is None
    assert validar_hora("1234") is None

def test_valida_hora_em_branco():
    assert validar_hora("    ") is None
    assert validar_hora("") is None