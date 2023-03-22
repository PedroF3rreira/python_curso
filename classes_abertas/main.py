from pessoa import Pessoa

p1 = Pessoa("pedro")
print(p1.nome)
p1.idade = 25
def get_nome(self):
    return self.nome


# adicionando método a classe pessoa usando nome da classe (Pessoa.nome_método)
Pessoa.get_nome = get_nome
print(p1.get_nome())
