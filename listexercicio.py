numeros = []

entrada = 1

while entrada > 0:
	entrada = int(input("Digite um numero "))
	
	if entrada != 0:
		numeros.append(entrada)

total = 1

for numero in numeros:
	total *= numero

print(f"A soma dos numero é {sum(numeros)}")
print(f"A multiplicação dos numero é {total}")
print(f"O menor dos numero é {min(numeros)}")
print(f"o maior dos numero é {max(numeros)}")