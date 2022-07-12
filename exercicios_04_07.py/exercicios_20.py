#20. Construa um script que leia o preço de um produto, o percentual de desconto e calcule o valor a pagar e o valor do desconto.
# Entrada: 10
# 10
# Saída:
# Total = 9
# Desconto = 1

valor = float(input("I1nforme o valor do produto: R$ "))
per = float(input("Informe o percentual de desconto: "))

desconto = (valor * per)/100
total = valor - desconto

print("O valor a pagar: ", total)
print("Valor do desconto: ", desconto)