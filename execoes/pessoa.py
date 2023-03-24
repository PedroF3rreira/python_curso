class Pessoa(object):
    def __init__(self):
        self.idade = 0

    def set_idade(self, idade):
        if idade < 18:
            raise ValueError("você é menor de idade!")
        else:
            self.idade = idade


try:
    idade = 10
    p = Pessoa()
    p.set_idade(idade)
except Exception as e:# pega messagem de error da classe Exception
    print("Ocorreu um erro ", e)
else:# caso o erro não ocorra
    print(f"você tem {idade} é maior de idade")
finally:# executa idependente se der erro ou não
    print("executando limpeza de cache")