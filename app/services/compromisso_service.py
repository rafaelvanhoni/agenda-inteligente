from app.core.models.compromisso import Compromisso
from app.validators import validador
from app.factories.compromisso_factory import CompromissoFactory
from datetime import datetime

def criar_compromisso() -> Compromisso | None:
    """
    Coleta e valida os dados de entrada do usuário, e delega a criação do compromisso à factory.
    
    Retorna:
    - Um objeto Compromisso se todos os dados forem válidos.
    - None se alguma etapa falhar.
    """        
    nome = validador.validar_obrigatorio(input("Nome: "), "Nome")
    if nome is None or not validador.validar_tamanho(nome, "Nome", 100):
        return None

    descricao = input("Descrição: ").strip()
    if not validador.validar_tamanho(descricao, "Descrição", 500):
        return None

    data_input = input("Data (dd/mm/aaaa): ")
    data = validador.validar_data(data_input)
    if not data:
        return None

    hora_input = input("Hora (hh:mm): ")
    hora = validador.validar_hora(hora_input)
    if not hora:
        return None
    
    local = input("Local: ")
    if not validador.validar_tamanho(local, "Local", 250):
        return None
    
    importante_input = input("Importante? (S/N): ")
    importante = validador.validar_bool(importante_input)
    if importante is None:
        return None

    concluido_input = input("Concluído? (S/N): ")
    concluido = validador.validar_bool(concluido_input)

    data_conclusao = None
    hora_conclusao = None

    if concluido:
        data_conclusao_input = input("Data Conclusão (dd/mm/yyyy): ")
        data_conclusao = validador.validar_data(data_conclusao_input)
        
        hora_conclusao_input = input("Hora Conclusão (hh:mm): ")
        hora_conclusao = validador.validar_hora(hora_conclusao_input)

        # Se for marcado como 'Concluído', mas o usuário não informar Data e Hora da Conclusão,
        # insere a data e hora atual automaticamente.
        if data_conclusao is None:
            agora = datetime.now()
            data_conclusao = agora.date()
            hora_conclusao = agora.time().replace(second=0, microsecond=0)

    return CompromissoFactory.criar(
            nome= nome,
            descricao= descricao,
            data= data,
            hora= hora,
            local= local,
            importante= importante,
            concluido= concluido,
            data_conclusao= data_conclusao,
            hora_conclusao= hora_conclusao        
    )

def editar_compromisso(compromisso: Compromisso) -> None:
    """
    Edita os campos de um objeto Compromisso, permitindo alterações seletivas.
    Campos deixados em branco permanecem com os valores atuais.
    """
    novo_nome = input(f"Nome [{compromisso.nome}]: ").strip()
    if novo_nome:
        if not validador.validar_tamanho(novo_nome, "Nome", 100):
            return None
        compromisso.nome = novo_nome

    nova_descricao = input(f"Descrição [{compromisso.descricao}]: ").strip()
    if nova_descricao:
        if not validador.validar_tamanho(nova_descricao, "Descrição", 500):
            return None
        compromisso.descricao = nova_descricao

    data_input = input(f"Data [{compromisso.data}] (dd/mm/aaaa): ").strip()
    if data_input:
        nova_data = validador.validar_data(data_input)
        if not nova_data:
            return None
        compromisso.data = nova_data

    hora_input = input(f"Hora [{compromisso.hora}] (hh:mm): ").strip()
    if hora_input:
        nova_hora = validador.validar_hora(hora_input)
        if not nova_hora:
            return None
        compromisso.hora = nova_hora
    
    novo_local = input(f"Local [{compromisso.local}]: ").strip()
    if novo_local:
        if not validador.validar_tamanho(novo_local, "Local", 250):
            return None
        compromisso.local = novo_local
    
    importante_input = input(f"Importante? [{compromisso.importante}] (S/N): ").strip()
    if importante_input:
        novo_importante = validador.validar_bool(importante_input)
        if novo_importante is None:
            return None
        compromisso.importante = novo_importante

    concluido_input = input(f"Concluído? [{compromisso.concluido}] (S/N): ").strip()
    if concluido_input:
        novo_concluido = validador.validar_bool(concluido_input)
        if novo_concluido is None:
            return None
        compromisso.concluido = novo_concluido
    
    data_conclusao_input = input(f"Data Conclusão [{compromisso.data_conclusao}] (dd/mm/yyyy): ").strip()
    if data_conclusao_input:
        nova_data_conclusao = validador.validar_data(data_conclusao_input)
        if not nova_data_conclusao:
            return None
        compromisso.data_conclusao = nova_data_conclusao
    
    hora_conclusao_input = input(f"Hora Conclusão [{compromisso.hora_conclusao}] (hh:mm): ").strip()
    if hora_conclusao_input:
        nova_hora_conclusao = validador.validar_hora(hora_conclusao_input)
        if not nova_hora_conclusao:
            return None
        compromisso.hora_conclusao = nova_hora_conclusao


def concluir_compromisso(compromisso: Compromisso) -> None:
    """
    Marca um compromisso como concluído, com data e hora fornecidos ou atuais.
    """
    print("\n>>> Marcando compromisso como concluído")

    usar_data_manual = input("Deseja informar a data e hora da conclusão manualmente? (S/N): ").strip()
    usar_data_manual = validador.validar_bool(usar_data_manual)
    if usar_data_manual is True:
        data_input = input("Data (dd/mm/aaaa): ")
        data = validador.validar_data(data_input)
        if not data:
            return None

        hora_input = input("Hora (hh:mm): ")
        hora = validador.validar_hora(hora_input)
        if not hora:
            return None
    else:
        agora = datetime.now()
        data = agora.date()
        hora = agora.time().replace(second=0, microsecond=0)   

    compromisso.concluido = True
    compromisso.data_conclusao = data
    compromisso.hora_conclusao = hora

    print("\n✅ Compromisso marcado como concluído")
