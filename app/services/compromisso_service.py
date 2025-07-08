from app.core.models import compromisso as model
from app.validators import validador
from app.factories import compromisso_factory as factory
from datetime import datetime

def criar_compromisso() -> model.Compromisso | None:
    """
    Coleta os dados do usuário, valida cada campo e cria um novo objeto Compromisso.

    Solicita informações como nome, descrição, data, hora, local, importância e conclusão.
    Se o compromisso estiver concluído, também coleta (ou gera) data e hora de conclusão.
    Utiliza a CompromissoFactory para instanciar o objeto.

    Retorna:
    - Compromisso: objeto criado com os dados fornecidos, se válidos.
    - None: se qualquer validação falhar durante o processo.
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
    if concluido is None:
        return None

    data_conclusao = None
    hora_conclusao = None

    if concluido:
        data_conclusao_input = input("Data Conclusão (dd/mm/yyyy): ")
        hora_conclusao_input = input("Hora Conclusão (hh:mm): ")

        validado, data_conclusao, hora_conclusao = tratar_conclusao(concluido, data_conclusao_input, hora_conclusao_input)
        
        if not validado:
            return None

    return factory.CompromissoFactory.criar(
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

def editar_compromisso(compromisso: model.Compromisso) -> None:
    """
    Permite ao usuário editar os campos de um compromisso existente.

    Cada campo é opcionalmente alterado, mantendo o valor atual se deixado em branco.
    Caso o campo 'Concluído?' seja alterado para verdadeiro, é solicitado o preenchimento
    (ou geração automática) da data e hora de conclusão.

    Parâmetros:
    - compromisso (Compromisso): objeto que será modificado.

    Retorna:
    - None: em caso de falha de validação, a edição é cancelada e o objeto permanece inalterado.
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

        data_conclusao_input = input(f"Data Conclusão [{compromisso.data_conclusao}] (dd/mm/yyyy): ").strip()
        hora_conclusao_input = input(f"Hora Conclusão [{compromisso.hora_conclusao}] (hh:mm): ").strip()

        validado, nova_data_conclusao, nova_hora_conclusao = tratar_conclusao(novo_concluido, data_conclusao_input, hora_conclusao_input)
        if not validado:
            return None
        
        compromisso.concluido = novo_concluido
        compromisso.data_conclusao = nova_data_conclusao
        compromisso.hora_conclusao = nova_hora_conclusao

def concluir_compromisso(compromisso: model.Compromisso) -> None:
    """
    Marca um compromisso como concluído, atualizando data e hora de conclusão.

    O usuário escolhe se deseja informar manualmente a data e hora, ou utilizar os valores atuais.
    A função valida os dados de conclusão antes de atualizar o objeto.

    Parâmetros:
    - compromisso (Compromisso): objeto a ser atualizado como concluído.

    Retorna:
    - None: se os dados de entrada forem inválidos.
    """
    print("\n>>> Marcando compromisso como concluído")

    usar_data_manual = input("Deseja informar a data e hora da conclusão manualmente? (S/N): ").strip()
    usar_data_manual = validador.validar_bool(usar_data_manual)
    if usar_data_manual:
        data_input = input("Data (dd/mm/aaaa): ")
        hora_input = input("Hora (hh:mm): ")

        validado, data, hora = tratar_conclusao(usar_data_manual, data_input, hora_input)        
        if not validado:
            return None
    elif usar_data_manual is None:
        return
    else:
        agora = datetime.now()
        data = agora.date()
        hora = agora.time().replace(second=0, microsecond=0)   

    compromisso.concluido = True
    compromisso.data_conclusao = data
    compromisso.hora_conclusao = hora

    print("\n✅ Compromisso marcado como concluído")

def tratar_conclusao(concluido: bool, data_input: str, hora_input: str):
    """
    Valida os campos de conclusão (data e hora) de um compromisso.

    Se os campos forem deixados em branco e o compromisso estiver concluído,
    a data/hora atuais são utilizadas. Se apenas um dos campos for preenchido,
    exibe mensagem de erro e retorna falha.

    Parâmetros:
    - concluido (bool): indica se o compromisso está concluído.
    - data_input (str): valor informado pelo usuário para a data de conclusão.
    - hora_input (str): valor informado pelo usuário para a hora de conclusão.

    Retorna:
    - Tuple (bool | None, date | None, time | None):
        - True + data/hora válidas, se os dados forem válidos.
        - False, None, None: se `concluido` for False.
        - None, None, None: se os dados forem inconsistentes ou inválidos.
    """    
    if not concluido:
        return False, None, None
    
    if not data_input and not hora_input:
        agora = datetime.now()
        return True, agora.date(), agora.time().replace(second=0, microsecond=0)
    
    if data_input and hora_input:
        data = validador.validar_data(data_input)
        hora = validador.validar_hora(hora_input)
        if data and hora:
            return True, data, hora
    
    print("⚠️  Informe **ambos** os campos de data e hora de conclusão ou deixe os dois em branco.")
    return None, None, None

def remover_compromisso(compromissos: list[model.Compromisso], compromisso: model.Compromisso) -> bool:
    """
    Remove um compromisso da lista, se estiver presente.

    Parâmetros:
    - compromissos (list): Lista original de compromissos.
    - compromisso (Compromisso): Compromisso a ser removido.

    Retorna:
    - True se a remoção foi bem-sucedida.
    - False se o compromisso não estiver na lista.
    """
    if compromisso in compromissos:
        compromissos.remove(compromisso)
        return True
    return False

def detalhar_compromisso(compromisso: model.Compromisso, titulo: str) -> None:
    if not compromisso:
        return None

    print(f"\n{titulo}")
    print(compromisso)
