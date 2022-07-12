# 2. Escreva um programa que leia 5 numeros e os armazene em um vetor. Mostre o vetor, o 
# maior elemento e a posição que ele se encontra.

vetor = []
maior = 0
menor = 0
posicao_maior = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

    if i == 0:
        maior = numero
        posicao_maior = numero
    elif numero > maior:
        maior = numero
        posicao_maior = i
    elif numero < menor:
        menor = numero
        posicao_menor = i



print(f"Vetor: {vetor}")
print(f"Maior: {maior}")
print(f"Posição maior: {posicao_maior}")
        
