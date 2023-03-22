class Aluno(object):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        self._idade = value





a = Aluno("elias", 54)
# a.nome = "pedro"
# a.idade = 29

print(a.nome, a.idade)