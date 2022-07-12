# 13. Escreva um script para ler um número e informar se ele é divisível por 5.

numero = int(input("Digite um número: "))
calculo = (numero % 5)
if calculo == 0:
    print(f"O número é divisível: ")
else:
    print(f"O número não é divisível: ")