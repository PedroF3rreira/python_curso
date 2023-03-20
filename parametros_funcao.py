# função vai receber o valor de uma lista
def soma(val1, val2, logic):
    if logic:
        print(f"A soma dos valores é {val1 + val2}")
    return val1 + val2


numbers = [5, 20, True]
# definindo parâmetro da função como uma lista se usa o * no inicio do parâmetro
soma(*numbers)


# função que recebe um parâmetro opcional marcado com *
def multiplica(val1, val2, *display):
    return val1 * val2
    if display:
        print(f"resultado {val1 * val2}")


# parâmetros nomeados não importa em que ordem nos os passamos
def dados_pessoas(nome, idade, peso, altura):
    print(f"nome: {nome}\nidade:{idade}\npeso:{peso}\naltura:{altura}")


dados_pessoas(idade="29", nome="pedro", altura="1.58", peso="85")
