salario = float(input("Digite o valor do salário "))
aumento = float(input("digite o valor do aumento "))

resultado = salario + (salario * aumento / 100)

print(f"O seu saláriio subiu para {resultado:,.2f}")