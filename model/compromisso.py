import uuid
from datetime import date, time, datetime

class Compromisso:
    def __init__(
            self, 
            nome: str, 
            descricao: str, 
            data: date, 
            hora: time, 
            local: str,
            importante: bool = False, 
            concluido: bool = False, 
            data_conclusao: date | None = None, 
            hora_conclusao: time | None = None
        ):
        """
        Inicializa um novo compromisso com os dados fornecidos.

        Parâmetros:
        - nome (str): título principal do compromisso (obrigatório)
        - descricao (str): descrição detalhada do compromisso
        - data (date): data agendada para o compromisso
        - hora (time): hora agendada para o compromisso
        - local (str): local onde ocorrerá o compromisso
        - importante (bool, opcional): marca se o compromisso é importante (default: False)
        - concluido (bool, opcional): indica se o compromisso foi concluído (default: False)
        - data_conclusao (date | None, opcional): data em que o compromisso foi concluído (default: None)
        - hora_conclusao (time | None, opcional): hora em que o compromisso foi concluído (default: None)
        """
        self.id = str(uuid.uuid4())        
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.local = local
        self.importante = importante
        self.concluido = concluido
        self.data_conclusao = data_conclusao
        self.hora_conclusao = hora_conclusao

    def __str__(self):
        """
        Retorna uma representação legível do compromisso.
        """        
        return f"{self.nome} em {self.data.strftime('%d/%m/%Y')} às {self.hora.strftime('%HH:%MM')}"