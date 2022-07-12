# 12. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math 
numero = float(input(f"Digite um número: "))
if numero > 0: 
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz}")
else:
    print("Número invalido!")