from datetime import date, time, datetime
from app.validators.validador import (
    validar_data, 
    validar_hora, 
    validar_data_hora, 
    validar_bool, 
    validar_obrigatorio, 
    validar_tamanho)

class TestValidarData:
    
    def test_valida(self):
        """
        Verifica se datas válidas no formato dd/mm/aaaa são convertidas corretamente em objetos date.
        """
        assert validar_data('01/10/2025') == date(2025, 10, 1)
        assert validar_data('05/12/2024') == date(2024, 12, 5)

    def test_invalida(self):
        """
        Verifica se entradas inválidas para data retornam None.
        """        
        assert validar_data('32/01/2025') is None
        assert validar_data('15/18/2025') is None
        assert validar_data(15) is None

    def test_em_branco(self):
        """
        Verifica se entradas em branco ou None são tratadas como inválidas para data.
        """        
        assert validar_data("   ") is None
        assert validar_data("") is None
        assert validar_data(None) is None

class TestValidarHora:

    def test_valida(self):
        """
        Verifica se horários válidos no formato HH:MM são convertidos corretamente em objetos time.
        """        
        assert validar_hora('12:00') == time(12, 0)
        assert validar_hora('08:30') == time(8, 30)
        assert validar_hora('23:59') == time(23, 59)
        assert validar_hora('00:00') == time(0, 0)

    def test_invalida(self):
        """
        Verifica se entradas inválidas para hora retornam None.
        """        
        assert validar_hora("27:15") is None
        assert validar_hora("13") is None
        assert validar_hora("1234") is None
        assert validar_hora(789) is None

    def test_em_branco(self):
        """
        Verifica se entradas em branco ou None são tratadas como inválidas para hora.
        """        
        assert validar_hora("    ") is None
        assert validar_hora("") is None
        assert validar_hora(153) is None
        assert validar_hora(None) is None

class TestValidarDataHora:

    def test_valida(self):
        """
        Verifica se entradas completas de data e hora no formato dd/mm/aaaa HH:MM são convertidas em datetime.
        """        
        assert validar_data_hora('01/10/2025 12:00') == datetime(2025, 10, 1, 12, 0)
        assert validar_data_hora('12/01/2024 08:30') == datetime(2024, 1, 12, 8, 30)

    def test_invalida(self):
        """
        Verifica se entradas inválidas para data e hora combinadas retornam None.
        """        
        assert validar_data_hora("31/02/2025 20:15") is None
        assert validar_data_hora("01/01/2024 13") is None
        assert validar_data_hora(22) is None

    def test_em_branco(self):
        """
        Verifica se entradas vazias ou None são tratadas como inválidas para data e hora combinadas.
        """        
        assert validar_data_hora("    ") is None
        assert validar_data_hora("") is None
        assert validar_data_hora(None) is None

class TestValidarBool:

    def test_verdadeiro(self):
        """
        Verifica se entradas que representam valores booleanos 'verdadeiros' retornam True.
        """        
        assert validar_bool('True') is True
        assert validar_bool('t') is True
        assert validar_bool('1') is True
        assert validar_bool('Sim') is True
        assert validar_bool('s') is True

    def test_falso(self):
        """
        Verifica se entradas que representam valores booleanos 'falsos' retornam False.
        """        
        assert validar_bool('não') is False
        assert validar_bool('Nao') is False
        assert validar_bool('F') is False
        assert validar_bool('False') is False
        assert validar_bool('n') is False
        assert validar_bool('0') is False

    def test_incorreto(self):   
        """
        Verifica se entradas que não representam valores booleanos retornam None.
        """        
        assert validar_bool(True) is None
        assert validar_bool(False) is None
        assert validar_bool(1) is None
        assert validar_bool("teste") is None

    def test_em_branco(self):
        """
        Verifica se entradas vazias ou None retornam None para validação booleana.
        """        
        assert validar_bool("") is None
        assert validar_bool("      ") is None
        assert validar_bool(None) is None

class TestValidarObrigatorio:

    def test_correto(self):
        """
        Verifica se campos preenchidos corretamente são aceitos pela validação obrigatória.
        """        
        assert validar_obrigatorio("entrada de dados", "nome_do_campo") == "entrada de dados"
        assert validar_obrigatorio("entrada de dados", "") == "entrada de dados"
        assert validar_obrigatorio("entrada de dados", ) == "entrada de dados"

    def test_incorreto(self):
        """
        Verifica se valores em branco ou inválidos são rejeitados pela validação obrigatória.
        """        
        assert validar_obrigatorio("   ", "nome_do_campo") is None
        assert validar_obrigatorio("", "nome_do_campo") is None
        assert validar_obrigatorio(True, "nome_do_campo") is None
        assert validar_obrigatorio(1, "nome_do_campo") is None
        assert validar_obrigatorio(None, "nome_do_campo") is None

class TestValidarTamanho:

    def test_correto(self):
        """
        Verifica se um campo dentro do limite de caracteres é aceito.
        """        
        assert validar_tamanho("dados informados em tela", "nome_do_campo", 50) is True

    def test_incorreto(self):
        """
        Verifica se campos que excedem o limite ou são inválidos são rejeitados.
        """        
        assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", 0) is False
        assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", -5) is False
        assert validar_tamanho("dados informados com varios caracteres", "nome_do_campo", 10) is False
        assert validar_tamanho(5, "nome_do_campo", 10) is False