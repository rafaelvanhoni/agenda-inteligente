from app.core.models.compromisso import Compromisso

class CompromissoFactory:
    
    @staticmethod
    def criar(nome, descricao, data, hora, local, importante, concluido, data_conclusao, hora_conclusao) -> Compromisso | None:
        """
        Cria uma nova instância de Compromisso com base nos dados já validados.

        Retorna:
        - Um objeto Compromisso.
        """
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



