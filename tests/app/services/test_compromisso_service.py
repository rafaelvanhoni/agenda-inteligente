import pytest
from app.core.models.compromisso import Compromisso
from app.services.compromisso_service import criar_compromisso, editar_compromisso, concluir_compromisso
from datetime import date, time, datetime, timedelta

class TestCriarCompromisso:
    def test_valido_nao_concluido(self, monkeypatch: pytest.MonkeyPatch): #1
        """
        Verifica se um compromisso válido e não concluído é criado corretamente.

        Esperado:
        - O compromisso deve ser criado com os dados fornecidos.
        - A flag 'concluído' deve ser False.
        - Nenhuma data ou hora de conclusão deve ser atribuída.
        """
        entradas = iter([
            "Reunião com equipe",        # Nome
            "Discutir as metas do mês",  # Descrição
            "01/10/2025",                # Data
            "14:30",                     # Hora
            "Sala 01",                   # Local
            "s",                         # Importante
            "n"                          # Concluído
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        compromisso = criar_compromisso()

        assert compromisso is not None
        assert compromisso.nome == "Reunião com equipe"
        assert compromisso.descricao == "Discutir as metas do mês"
        assert compromisso.data == date(2025, 10, 1)
        assert compromisso.hora == time(14, 30)
        assert compromisso.local == "Sala 01"
        assert compromisso.importante is True
        assert compromisso.concluido is False

    def test_valido_concluido_sem_informar_data(self, monkeypatch: pytest.MonkeyPatch): #2
        """
        Verifica se um compromisso marcado como concluído, mas sem data/hora informadas,
        utiliza a data e hora atual do sistema.

        Esperado:
        - O compromisso deve ser criado com os dados fornecidos.
        - A flag 'concluído' deve ser True.
        - A data e hora de conclusão devem ser preenchidas automaticamente com a data/hora atual.
        """
        entradas = iter([
            "Reunião com equipe",        # Nome
            "Discutir as metas do mês",  # Descrição
            "01/10/2025",                # Data
            "14:30",                     # Hora
            "Sala 01",                   # Local
            "s",                         # Importante
            "Sim",                       # Concluído
            "",                          # Data Conclusão
            ""                           # Hora Conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        compromisso = criar_compromisso()

        assert compromisso is not None
        assert compromisso.nome == "Reunião com equipe"
        assert compromisso.descricao == "Discutir as metas do mês"
        assert compromisso.data == date(2025, 10, 1)
        assert compromisso.hora == time(14, 30)
        assert compromisso.local == "Sala 01"
        assert compromisso.importante is True
        assert compromisso.concluido is True

        agora = datetime.now()
        toleracia = timedelta(seconds=5)

        data_minima = (agora - toleracia).date()
        hora_minima = (agora - toleracia).time().replace(second=0, microsecond=0)

        assert compromisso.data_conclusao >= data_minima
        assert compromisso.hora_conclusao >= hora_minima

    def test_falha_quando_so_data_conclusao_eh_informada(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #3
        """
        Verifica se a criação falha ao informar apenas a data de conclusão sem a hora.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida uma mensagem de erro solicitando ambos os campos: data e hora.
        """  
        entradas = iter([
            "Reunião com equipe",        # Nome
            "Discutir as metas do mês",  # Descrição
            "01/10/2025",                # Data
            "14:30",                     # Hora
            "Sala 01",                   # Local
            "s",                         # Importante
            "Sim",                       # Concluído
            "05/10/2025",                # Data Conclusão
            ""                           # Hora Conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "Informe **ambos** os campos de data e hora de conclusão" in captured.out

    def test_falha_quando_so_hora_conclusao_eh_informada(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #4
        """
        Verifica se a criação falha ao informar apenas a hora de conclusão sem a data.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida uma mensagem de erro solicitando ambos os campos: data e hora.
        """   
        entradas = iter([
            "Reunião com equipe",        # Nome
            "Discutir as metas do mês",  # Descrição
            "01/10/2025",                # Data
            "14:30",                     # Hora
            "Sala 01",                   # Local
            "s",                         # Importante
            "Sim",                       # Concluído
            "",                          # Data Conclusão
            "15:30"                      # Hora Conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "Informe **ambos** os campos de data e hora de conclusão" in captured.out

    def test_falha_quando_concluido_invalido(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #5
        """
        Verifica se a criação falha ao informar um valor inválido para o campo 'concluído'.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida uma mensagem solicitando uma resposta válida (sim/não).
        """
        entradas = iter([
            "Revisão final",           # Nome
            "Revisar contratos",       # Descrição
            "20/10/2025",              # Data
            "16:00",                   # Hora
            "Escritório",              # Local
            "s",                       # Importante
            "talvez"                   # Concluído inválido
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "Informe 'sim' ou 'não'" in captured.out

    def test_criar_compromisso_falha_nome_em_branco(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #6
        """
        Testa a falha na criação de um compromisso quando o campo 'Nome' é deixado em branco.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida a mensagem de erro correspondente ao campo obrigatório.
        """
        entradas = iter([
            "",                          # Nome (inválido)
            "Descrição qualquer",        # Descrição
            "01/10/2025",                # Data
            "14:00",                     # Hora
            "Sala X",                    # Local
            "s",                         # Importante
            "n"                          # Concluído
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "O campo 'Nome' é obrigatório." in captured.out

    def test_criar_compromisso_falha_descricao_muito_longa(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #7
        """
        Testa a falha na criação de um compromisso quando a descrição ultrapassa 500 caracteres.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida a mensagem de erro de tamanho excedido.
        """
        descricao_longa = "A" * 501
        entradas = iter([
            "Compromisso",
            descricao_longa,             # Descrição (inválida)
            "01/10/2025",
            "14:00",
            "Sala X",
            "s",
            "n"
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "O campo 'Descrição' tem um tamanho máximo de 500 caracteres." in captured.out

    def test_criar_compromisso_falha_hora_invalida(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #8
        """
        Testa a falha na criação de um compromisso quando a hora está em formato inválido.

        Esperado:
        - O compromisso não deve ser criado.
        - Deve ser exibida a mensagem indicando formato de hora inválido.
        """
        entradas = iter([
            "Compromisso",
            "Descrição válida",
            "01/10/2025",
            "25:00",                     # Hora inválida
            "Sala X",
            "s",
            "n"
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))
        compromisso = criar_compromisso()
        captured = capsys.readouterr()

        assert compromisso is None
        assert "Utilize a formatação 'hh:mm'" in captured.out    

class TestEditarCompromisso:

    def test_todos_os_campos(self, monkeypatch: pytest.MonkeyPatch): #9
        """
        Verifica se todos os campos de um compromisso são atualizados corretamente durante a edição.

        Esperado:
        - Todos os campos devem ser substituídos pelos novos valores informados.
        - O compromisso deve ser marcado como concluído com data e hora de conclusão válidas.
        """ 
        compromisso = Compromisso(
            nome="Compromisso Antigo",
            descricao="Descrição antiga",
            data=date(2025, 10, 1),
            hora=time(14, 0),
            local="Sala A",
            importante=False,
            concluido=False,
            data_conclusao=None,
            hora_conclusao=None
        )

        entradas = iter([
            "Revisão Geral",          # Novo nome
            "Revisar documentos",     # Nova descrição
            "02/10/2025",             # Nova data
            "15:30",                  # Nova hora
            "Sala B",                 # Novo local
            "s",                      # Importante
            "s",                      # Concluído
            "03/10/2025",             # Data conclusão
            "16:00"                   # Hora conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        editar_compromisso(compromisso)

        assert compromisso.nome == "Revisão Geral"
        assert compromisso.descricao == "Revisar documentos"
        assert compromisso.data == date(2025, 10, 2)
        assert compromisso.hora == time(15, 30)
        assert compromisso.local == "Sala B"
        assert compromisso.importante is True
        assert compromisso.concluido is True
        assert compromisso.data_conclusao == date(2025, 10, 3)
        assert compromisso.hora_conclusao == time(16, 0)   

    def test_parcial(self, monkeypatch: pytest.MonkeyPatch): #10
        """
        Verifica se a edição parcial mantém os valores originais dos campos não preenchidos
        e atualiza apenas os campos informados.

        Esperado:
        - Apenas os campos com nova entrada devem ser alterados.
        - Os demais campos devem manter seus valores originais.
        """
        compromisso = Compromisso(
            nome="Reunião inicial",
            descricao="Definir escopo do projeto",
            data=date(2025, 10, 5),
            hora=time(9, 0),
            local="Sala 02",
            importante=False,
            concluido=False
        )

        entradas = iter([
            "",                     # Nome (mantém)
            "",                     # Descrição (mantém)
            "",                     # Data (mantém)
            "",                     # Hora (mantém)
            "Sala 03",              # Local (novo)
            "s",                    # Importante (novo)
            "",                     # Concluído (mantém)
            "",                     # Data conclusão (mantém)
            ""                      # Hora conclusão (mantém)
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        editar_compromisso(compromisso)

        assert compromisso.nome == "Reunião inicial"
        assert compromisso.descricao == "Definir escopo do projeto"
        assert compromisso.data == date(2025, 10, 5)
        assert compromisso.hora == time(9, 0)
        assert compromisso.local == "Sala 03"                # alterado
        assert compromisso.importante is True                # alterado
        assert compromisso.concluido is False    


    def test_falha_nome_maior_que_limite(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #11
        """
        Verifica se a edição falha ao tentar alterar o nome para um valor com mais de 100 caracteres.

        Esperado:
        - O nome original deve ser preservado.
        - Deve ser exibida uma mensagem de erro sobre o limite de caracteres.
        """ 
        compromisso = Compromisso(
            nome="Nome válido",
            descricao="Descrição qualquer",
            data=date(2025, 11, 1),
            hora=time(10, 0),
            local="Sala X",
            importante=False,
            concluido=False
        )

        nome_muito_longo = "A" * 101  # 101 caracteres
        entradas = iter([
            nome_muito_longo,  # Nome (inválido)
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        editar_compromisso(compromisso)
        captured = capsys.readouterr()

        assert "O campo 'Nome' tem um tamanho máximo de 100 caracteres." in captured.out
        assert compromisso.nome == "Nome válido"  # Não alterado    

    def test_concluir_com_data_hora(self, monkeypatch: pytest.MonkeyPatch): #12
        """
        Verifica se a conclusão de um compromisso funciona corretamente ao informar
        data e hora de conclusão.

        Esperado:
        - O compromisso deve ser marcado como concluído.
        - Os campos de data e hora de conclusão devem ser preenchidos corretamente.
        """  
        compromisso = Compromisso(
            nome="Visita técnica",
            descricao="Avaliar estrutura",
            data=date(2025, 9, 10),
            hora=time(9, 0),
            local="Obra A",
            importante=False,
            concluido=False
        )

        entradas = iter([
            "",                      # Nome (mantém)
            "",                      # Descrição (mantém)
            "",                      # Data (mantém)
            "",                      # Hora (mantém)
            "",                      # Local (mantém)
            "",                      # Importante (mantém)
            "s",                     # Concluído
            "15/09/2025",            # Data conclusão
            "17:30"                  # Hora conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        editar_compromisso(compromisso)

        assert compromisso.concluido is True
        assert compromisso.data_conclusao == date(2025, 9, 15)
        assert compromisso.hora_conclusao == time(17, 30)    

    def test_falha_conclusao_com_apenas_data(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]): #13
        """
        Verifica se a edição falha ao tentar concluir um compromisso com apenas a data,
        sem informar a hora.

        Esperado:
        - O compromisso não deve ser marcado como concluído.
        - Os campos de data e hora de conclusão devem permanecer vazios.
        - Deve ser exibida mensagem solicitando ambos os campos.
        """
        compromisso = Compromisso(
            nome="Acompanhamento",
            descricao="Reunião com cliente",
            data=date(2025, 10, 5),
            hora=time(10, 0),
            local="Sala 2",
            importante=True,
            concluido=False
        )

        entradas = iter([
            "",               # Nome
            "",               # Descrição
            "",               # Data
            "",               # Hora
            "",               # Local
            "",               # Importante
            "s",              # Concluído
            "10/10/2025",     # Data conclusão (preenchida)
            ""                # Hora conclusão (faltando)
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        editar_compromisso(compromisso)
        captured = capsys.readouterr()

        # Deve permanecer não concluído
        assert compromisso.concluido is False
        assert compromisso.data_conclusao is None
        assert compromisso.hora_conclusao is None
        assert "Informe **ambos** os campos de data e hora de conclusão" in captured.out    

class TestConcluir:
    def test_com_data_hora_validas(self, monkeypatch: pytest.MonkeyPatch):
        """
        Verifica se um compromisso é corretamente marcado como concluído
        ao informar manualmente data e hora válidas.

        Esperado:
        - O compromisso deve ser marcado como concluído.
        - A data e hora de conclusão devem ser atribuídas corretamente.
        """
        compromisso = Compromisso(
            nome="Reunião técnica",
            descricao="Ajustes finais no projeto",
            data=date(2025, 9, 30),
            hora=time(10, 0),
            local="Sala 01",
            importante=False,
            concluido=False
        )

        entradas = iter([
            "s",                # Deseja informar manualmente?
            "30/09/2025",       # Data de conclusão
            "11:15"             # Hora de conclusão
        ])

        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        concluir_compromisso(compromisso)

        assert compromisso.concluido is True
        assert compromisso.data_conclusao == date(2025, 9, 30)
        assert compromisso.hora_conclusao == time(11, 15)    

    def test_com_data_hora_automaticas(self, monkeypatch: pytest.MonkeyPatch):
        """
        Verifica se um compromisso é concluído automaticamente com a data e hora atual
        ao optar por não informar os valores manualmente.

        Esperado:
        - O compromisso deve ser marcado como concluído.
        - A data e hora de conclusão devem ser atribuídas com base no horário do sistema.
        """
        compromisso = Compromisso(
            nome="Apresentação",
            descricao="Palestra sobre IA",
            data=date(2025, 10, 10),
            hora=time(14, 0),
            local="Auditório",
            importante=True,
            concluido=False
        )

        entradas = iter([
            "n"  # Deseja informar manualmente?
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        from app.services.compromisso_service import concluir_compromisso
        antes = datetime.now()
        concluir_compromisso(compromisso)
        depois = datetime.now()

        assert compromisso.concluido is True
        assert compromisso.data_conclusao >= antes.date()
        assert compromisso.data_conclusao <= depois.date()

        hora_min = antes.time().replace(second=0, microsecond=0)
        hora_max = depois.time().replace(second=0, microsecond=0)

        assert hora_min <= compromisso.hora_conclusao <= hora_max    

    def test_falha_com_apenas_data(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
        """
        Verifica se a conclusão falha quando apenas a data de conclusão é informada,
        sem a hora correspondente.

        Esperado:
        - O compromisso não deve ser marcado como concluído.
        - Deve ser exibida uma mensagem solicitando ambos os campos: data e hora.
        """
        compromisso = Compromisso(
            nome="Planejamento",
            descricao="Planejar cronograma",
            data=date(2025, 11, 1),
            hora=time(10, 0),
            local="Sala de reunião",
            importante=False,
            concluido=False
        )

        entradas = iter([
            "s",              # Deseja informar manualmente?
            "01/11/2025",     # Data de conclusão
            ""                # Hora de conclusão em branco
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        from app.services.compromisso_service import concluir_compromisso
        concluir_compromisso(compromisso)
        captured = capsys.readouterr()

        assert compromisso.concluido is False
        assert compromisso.data_conclusao is None
        assert compromisso.hora_conclusao is None
        assert "Informe **ambos** os campos de data e hora de conclusão" in captured.out    

    def test_falha_com_apenas_hora(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
        """
        Verifica se a conclusão falha quando apenas a hora de conclusão é informada,
        sem a data correspondente.

        Esperado:
        - O compromisso não deve ser marcado como concluído.
        - Deve ser exibida uma mensagem solicitando ambos os campos: data e hora.
        """
        compromisso = Compromisso(
            nome="Revisão de código",
            descricao="Revisar funcionalidades pendentes",
            data=date(2025, 11, 2),
            hora=time(14, 0),
            local="Home Office",
            importante=True,
            concluido=False
        )

        entradas = iter([
            "sim",     # Deseja informar manualmente?
            "",        # Data de conclusão em branco
            "17:00"    # Hora de conclusão
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        from app.services.compromisso_service import concluir_compromisso
        concluir_compromisso(compromisso)
        captured = capsys.readouterr()

        assert compromisso.concluido is False
        assert compromisso.data_conclusao is None
        assert compromisso.hora_conclusao is None
        assert "Informe **ambos** os campos de data e hora de conclusão" in captured.out    

    def test_falha_com_resposta_invalida(self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
        """
        Verifica se a conclusão falha quando é informada uma resposta inválida
        na pergunta sobre usar data/hora manual.

        Esperado:
        - O compromisso não deve ser marcado como concluído.
        - Deve ser exibida uma mensagem indicando que a resposta deve ser 'sim' ou 'não'.
        """
        compromisso = Compromisso(
            nome="Entrega de relatório",
            descricao="Finalizar e enviar relatório mensal",
            data=date(2025, 11, 5),
            hora=time(11, 0),
            local="Sala 4",
            importante=False,
            concluido=False
        )

        entradas = iter([
            "depende"  # Resposta inválida
        ])
        monkeypatch.setattr("builtins.input", lambda _: next(entradas))

        from app.services.compromisso_service import concluir_compromisso
        concluir_compromisso(compromisso)
        captured = capsys.readouterr()

        assert compromisso.concluido is False
        assert compromisso.data_conclusao is None
        assert compromisso.hora_conclusao is None
        assert "Informe 'sim' ou 'não'" in captured.out    