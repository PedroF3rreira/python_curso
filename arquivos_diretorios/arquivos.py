file = open('texto.txt', 'a')
file.write("Escrevendo uma lina\n")

file = open('texto.txt', 'r')

# lendo o arquivo completo
print(file.read())

file.close()

file = open('texto.txt', 'r')
# lendo o arquivo linha a linha


for linha in file.readlines():
    print(f"linha - {linha}")

file.close()

file = open('texto2.txt', 'w')

linhas = ['pedro\n', 'elias\n', 'moises\n', 'sandra\n', 'camila\n', 'edson\n']

file.writelines(linhas)
file.close()

# utilizando o with ele fecha automaticamento o arquivo
with open('texto2.txt', 'r') as file:
    print("lendo arquivo com com with ")
    print(file.read())
