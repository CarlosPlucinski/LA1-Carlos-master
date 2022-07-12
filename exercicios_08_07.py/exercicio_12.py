# 12. Construa um programa que leia vários valores númericos enquanto um valor negativo não for digitado. Após isso, mostre a média aritmética dos valores recebidos.
# Entrada:
# 3
# 5
# 10
# -1
# Saída:
# 6

soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor: "))

    if valor < 0:
        break
    
    soma += valor
    contador += 1

media = soma / contador
print(f"A média dos valores digitador é: {media:.2f}")

