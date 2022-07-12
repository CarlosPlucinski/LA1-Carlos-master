# 3. Faça um programa que receba do usuario um vetor com 5 posições. Em seguida, mostre
# o maior e o menor elemento do vetor.

vetor = []
posicao_menor = 0
posicao_maior = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

    if i == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
        posicao_maior = i
    elif numero < menor:
        menor = numero
        posicao_menor = i

print(f"Vetor: {vetor}")
print(f"Maior: {maior}")
print(f"Posição maior: {posicao_maior}")
print(f"Menor: {menor}")
print(f"Posição menor: {posicao_menor}")

