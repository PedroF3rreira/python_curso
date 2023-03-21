class Ponto():
    x = 10
    y = 7
    def imprime_x(self):
        print(f"imprimindo: {self.x}")


p = Ponto()
print(p.x) # 10 (do atributo da classe) está acessando atributo da classe
print(p.y) # 7 (do atributo da classe)  está acessando atributo da classe
p.x = 12 # p obtém seu próprio atributo "x" agora definiu o atributo x do objeto
print(p.x) # 12 (encontrado na instância) imprime atributo do objeto
print(Ponto.x) # 10 (O atributo da classe ainda é o mesmo) imprime atributo da classe
del p.x # Apagando o atributo da instância
print(p.x) # 10 (Agoa que não existe "x" na instância, será retornado da classe) imprime atributo da classe
p.z = 3 # define atributo z para o objeto
print(p.z) # 3
print(Ponto.z) # Ponto.z tenta acessar menbro de classe z mas não existe pois ele só foi definido dinamicamente
               # no objeto p nao na classe Ponto



# forma de acessar atributo menbroi de classe
Ponto.x
