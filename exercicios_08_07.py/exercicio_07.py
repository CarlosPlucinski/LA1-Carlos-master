# Faça um programa que receba um número N e mostre na tela todos os números ímpares de 0 até N.
# Entrada: 5
# Saída: 1, 3, 5

numero = int(input("Digite um número: "))

for i in range(1, numero + 1, 2):
        print(i)

        # OU:

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    if i % 2 == 0:
        continue
    print(i)