class Compromisso:
    def __init__(self, nome, data):
        """
        Representa um compromisso com nome e data.

        Atributos:
        - nome (str): nome ou descrição do compromisso
        - data (datetime): data e hora do compromisso
        """        
        self.nome = nome
        self.data = data

    def __str__(self):
        """
        Retorna uma representação legível do compromisso.
        """        
        return f"Nome: {self.nome}, Data: {self.data}"