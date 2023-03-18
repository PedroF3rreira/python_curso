nome = input("digite o nome do aluno ")
notas = []
i = 0

while i < 4:
	notas.append(float(input("digite a nota do aluno ")))
	i += 1

media = (sum(notas)) / 5

if media >= 7:
	print(f"O aluno {nome} está aprovado sua média é de {media:,.2f}")
elif media >= 5 and media < 7:
	print(f"O aluno {nome} está de recuperação sua média é de {media:,.2f}")
else:
	print(f"O aluno {nome} está de reprovado sua média é de {media:,.2f}")
