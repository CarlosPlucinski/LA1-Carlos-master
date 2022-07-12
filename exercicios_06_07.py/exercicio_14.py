# 14. Leia um número. Se o número for positivo imprima a raiz quadrada desse número. Do contrário, imprima o número ao quadrado.

numero = int(input("Digite um número: "))
raiz = numero ** (1/2)
quadrado = numero ** 2
if numero > 0: 
    print(f"A raiz quadrada desse número é: {raiz}")
else:
    print(f"Número ao quadrado {quadrado}")
