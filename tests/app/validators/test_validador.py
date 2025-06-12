from datetime import date, time, datetime
from app.validators.validador import (
    validar_data, 
    validar_hora, 
    validar_data_hora, 
    validar_bool, 
    validar_obrigatorio, 
    validar_tamanho)

# validar_data
def test_validar_data_valida():
    assert validar_data('01/10/2025') == date(2025, 10, 1)
    assert validar_data('05/12/2024') == date(2024, 12, 5)

def test_validar_data_invalida():
    assert validar_data('32/01/2025') is None
    assert validar_data('15/18/2025') is None
    assert validar_data(15) is None

def test_validar_data_em_branco():
    assert validar_data("   ") is None
    assert validar_data("") is None
    assert validar_data(None) is None

# validar hora
def test_validar_hora_valida():
    assert validar_hora('12:00') == time(12, 0)
    assert validar_hora('08:30') == time(8, 30)
    assert validar_hora('23:59') == time(23, 59)
    assert validar_hora('00:00') == time(0, 0)

def test_validar_hora_invalida():
    assert validar_hora("27:15") is None
    assert validar_hora("13") is None
    assert validar_hora("1234") is None
    assert validar_hora(789) is None

def test_validar_hora_em_branco():
    assert validar_hora("    ") is None
    assert validar_hora("") is None
    assert validar_hora(153) is None
    assert validar_hora(None) is None


# validar data_hora
def test_validar_data_hora_valida():
    assert validar_data_hora('01/10/2025 12:00') == datetime(2025, 10, 1, 12, 0)
    assert validar_data_hora('12/01/2024 08:30') == datetime(2024, 1, 12, 8, 30)

def test_validar_data_hora_invalida():
    assert validar_data_hora("31/02/2025 20:15") is None
    assert validar_data_hora("01/01/2024 13") is None
    assert validar_data_hora(22) is None

def test_validar_data_hora_em_branco():
    assert validar_data_hora("    ") is None
    assert validar_data_hora("") is None
    assert validar_data_hora(None) is None

# validar bool
def test_validar_bool_verdadeiro():
    assert validar_bool('True') is True
    assert validar_bool('t') is True
    assert validar_bool('1') is True
    assert validar_bool('Sim') is True
    assert validar_bool('s') is True

def test_validar_bool_falso():
    assert validar_bool('não') is False
    assert validar_bool('Nao') is False
    assert validar_bool('F') is False
    assert validar_bool('False') is False
    assert validar_bool('n') is False
    assert validar_bool('0') is False

def test_validar_bool_incorreto():   
    assert validar_bool(True) is None
    assert validar_bool(False) is None
    assert validar_bool(1) is None
    assert validar_bool("teste") is None

def test_validar_bool_em_branco():
    assert validar_bool("") is None
    assert validar_bool("      ") is None
    assert validar_bool(None) is None

# validar obrigatório
def test_validar_obrigatorio_correto():
    assert validar_obrigatorio("entrada de dados", "nome_do_campo") == "entrada de dados"
    assert validar_obrigatorio("entrada de dados", "") == "entrada de dados"
    assert validar_obrigatorio("entrada de dados", ) == "entrada de dados"

def test_validar_obrigatorio_incorreto():
    assert validar_obrigatorio("   ", "nome_do_campo") is None
    assert validar_obrigatorio("", "nome_do_campo") is None
    assert validar_obrigatorio(True, "nome_do_campo") is None
    assert validar_obrigatorio(1, "nome_do_campo") is None
    assert validar_obrigatorio(None, "nome_do_campo") is None

# validar tamanho    
def test_validar_tamanho_correto():
    assert validar_tamanho("dados informados em tela", "nome_do_campo", 50) is True

def test_validar_tamanho_incorreto():
    assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", 0) is False
    assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", -5) is False
    assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", 10) is False
    assert validar_tamanho(5, "nome_do_campo", 10) is False