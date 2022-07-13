# 16. Crie um script que leia 5 valores e mostre qual o maior e o menor valor lido.
# Entrada:
# -1
# 0
# 9
# 2
# 3
# Saída:
# O menor valor digitado foi -1
# O maior valor digitado foi 9


maior_valor, menor_valor = None, None

for i in range(5):
    valor = float(input("Digite um valor: "))

    if i == 0:
        maior_valor = valor
        menor_valor = valor
    elif valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor

print(menor_valor, maior_valor)

