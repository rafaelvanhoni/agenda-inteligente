from model.compromisso import Compromisso
from datetime import datetime
import validador

class CompromissoFactory:
    
    @classmethod
    def criar(cls) -> Compromisso | None:
        """
        Cria uma nova instância de Compromisso com base nos dados informados pelo usuário.

        Retorna:
        - Um objeto Compromisso se todas as validações forem bem-sucedidas.
        - None se alguma etapa falhar.
        """
        nome = validador.validar_obrigatorio(input("Nome: "), "Nome")
        if nome is None or not validador.validar_tamanho(nome, "Nome", 100):
            return None

        descricao = input("Descrição: ").strip()
        if not validador.validar_tamanho(descricao, "Descrição", 500):
            return None

        data = input("Data (dd/mm/aaaa): ")
        data = validador.validar_data(data)
        if not data:
            return None

        hora = input("Hora (hh:mm): ")
        hora = validador.validar_hora(hora)
        if not hora:
            return None
        
        local = input("Local: ")
        if not validador.validar_tamanho(local, "Local", 250):
            return None
        
        importante = input("Importante? (S/N): ")
        importante = validador.validar_bool(importante)
        if importante is None:
            return None

        concluido = input("Concluído? (S/N): ")
        concluido = validador.validar_bool(concluido)

        data_conclusao = input("Data Conclusão (dd/mm/yyyy): ")
        data_conclusao = validador.validar_data(data_conclusao)
        
        hora_conclusao = input("Hora Conclusão (hh:mm): ")
        hora_conclusao = validador.validar_hora(hora_conclusao)

        # Se for marcado como 'Concluído', mas o usuário não informar Data e Hora da Conclusão,
        # insere a data e hora atual automaticamente.
        if concluido is True and data_conclusao is None:
            agora = datetime.now()
            data_conclusao = agora.date()
            hora_conclusao = agora.time().replace(second=0, microsecond=0)

        return Compromisso(
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


