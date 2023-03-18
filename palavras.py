palavras = []
entrada = "1"

while entrada != "0":
	entrada = input("Digite uma palavra ")
	
	if entrada != "0":
		palavras.append(entrada)

busca = input("digite uma palavra da sua lista")

for palavra in palavras:
	print(palavra)

if busca in palavras:
	print(f"essa palavra tem {len(busca)} ocorrencias")
else:
	print("essa palavra não foi encontrada")
