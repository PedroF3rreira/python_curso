class Calculo():
    def calcula_total(self, qtd, desc):
        return (self.preco * qtd - desc)

cal = Calculo()
cal.preco = 25
print(cal.calcula_total(10, 58))#executando método utilizando propiedade de objeto
print(Calculo.calcula_total(cal, 10, 25))# executando método pela classe temos que passar o objeto pois a classe
                                        # não têm a propiedade preco que pertebce a o escopo do objeto
