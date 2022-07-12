# 05. Escreva um script que receba um número, se esse número for ímpar mostre na tela o quadrado do número digitado. No final do script mostrar na tela "Programa finalizado..."

# Exemplo 01
# Entrada:
# 10
# Saída:
# 5
# Programa finalizado...

# Exemplo 02
# Entrada:
# 9
# Saída:
# Programa finalizado...

numero =  int(input("Informe um valor: "))
if numero % 2 == 0:
    print("Programa finalizado!")
else:
    print(numero * numero) 
    print("Programa finalizado!")