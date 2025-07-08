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
        Retorna uma representação completa e formatada do compromisso.

        A saída inclui:
        - Nome
        - Descrição
        - Local
        - Data e hora do compromisso
        - Indicação de importância ("Sim"/"Não")
        - Indicação de conclusão ("Sim"/"Não")
        - Data e hora de conclusão (se houver)

        Retorna:
        - str: uma descrição detalhada e legível do compromisso
        """
        data_str = self.data.strftime('%d/%m/%Y')
        hora_str = self.hora.strftime('%H:%M')
        importante_str = "Sim" if self.importante else "Não"
        concluido_str = "Sim" if self.concluido else "Não"

        data_conc_str = self.data_conclusao.strftime('%d/%m/%Y') if self.data_conclusao else "-----"
        hora_conc_str = self.hora_conclusao.strftime('%H:%M') if self.hora_conclusao else "-----"

        return (
            f"Nome: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"Local: {self.local}\n"
            f"Data: {data_str}\n"
            f"Hora: {hora_str}\n"
            f"Importante: {importante_str}\n"
            f"Concluído: {concluido_str}\n"
            f"Data de conclusão: {data_conc_str}\n"
            f"Hora de conclusão: {hora_conc_str}"
        )
    
    def resumo(self):
        """
        Retorna um resumo formatado do compromisso.

        O resumo inclui:
        - Nome (limitado a 20 caracteres)
        - Data no formato 'dd/mm/yyyy'
        - Hora no formato 'HH:MM'
        - Indicação textual se é importante ("Sim"/"Não")
        - Indicação textual se está concluído ("Sim"/"Não")

        Retorna:
        - str: uma linha com os dados resumidos do compromisso
        """
        nome_resumido = self.nome[:20]
        data_str = self.data.strftime('%d/%m/%Y')
        hora_str = self.hora.strftime('%H:%M')
        importante_str = "Sim" if self.importante else "Não"
        concluido_str = "Sim" if self.concluido else "Não"
        
        return f"{nome_resumido} em {data_str} às {hora_str} | Importante: {importante_str} | Concluído: {concluido_str}"