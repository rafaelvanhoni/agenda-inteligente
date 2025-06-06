class Compromisso:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data

    def __str__(self):
        return f"Nome: {self.nome}, Data: {self.data}"