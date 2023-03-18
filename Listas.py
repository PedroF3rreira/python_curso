bancos = ['banco brasil', 'bradesco', 'itau', 'caixa econômica']

bancos += ['banco do sul', 'banco central']

#adiciona um item na lista
bancos.append("bando alagoinha do norte")

#insert adiciona um item no indice desejado
bancos.insert(2, 'primeiro banco')

#removendo um item
bancos.remove('banco do sul')

print(len(bancos))


for banco in bancos:
	print(f"meus bancos: {banco}")