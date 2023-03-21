# verificar se string começa com a letra passada
nome = "Pedro Daniel da silva"

if nome.startswith("Pedro"):
    print("esta string começa com a letra (Pedro)")
if nome.endswith("a"):
    print("esta string termina com a letra (silva)")

# podemos ter acesso a os caracteres de uma string pelos seus indices pois string é um objeto iterator
print(nome[3])
print("imprime cada caractere da string")
for letra in nome:
    print(letra)

# verifica se uma palavra esta contida na string com operador (in)
result = "Pedro" in nome
print(result)

# verifica se a palavra não esta contida na string
result = "Elias" not in nome
print(result)

# converter maiúsculo e minúsculo
print(nome.upper())
print(nome.lower())

# contar quantas vezes a palavra se repete num frase
frase = "se eu pode-se teria vivido mais amado mais se arriscado ainda mais"
print(frase.count("se"))

contador = 0
palavra = input("digite uma palavra ")
nome_arquivo = "python.txt"

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        contador = contador + linha.upper().count(palavra.upper())

print(f"A palavra pesquisada é {palavra}")
print(f"Foram encontradas {str(contador)}")
print(f"Arquivo pesquisado {nome_arquivo}")

# podemos usar o método find e rfind
print(nome.find("Pedro"))

# centralizando saida de string
textos = ["português", "inglês", "matemática", "geografia"]

for texto in textos:
    print(texto.center(30, "*"))

print("\n\n")

# alinhamento a esquerda e a direita
for texto in textos:
    if (textos.index(texto) % 2) == 1:
        print(texto.ljust(30, "*"))
    else:
        print(texto.rjust(30, "*"))

# utilizando split para gerar uma lista com palavras separadas por um caracter
csv_header = "produto; quantidade; valor"
csv_body = "arroz;10;5.9\nmacarrão;5;2.90"

lista1 = csv_header.split(";")
lista2 = csv_body.splitlines()
lista3 = []

for linha in lista2:
    lista3.append(linha.split(";"))


print(lista1)
print(lista2)
print(lista3)

for list in lista3:
    for item in list:
        print(item)
