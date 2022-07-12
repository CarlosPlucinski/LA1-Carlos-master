# 06. Escreva um script que receba um número, se esse número for par mostre na tela "O número é par" senão mostre "O número é ímpar".

# Exemplo 01
# Entrada:
# 10
# Saída: O número é par

# Exemplo 02
# Entrada:
# 9
# Saída: O número é par

# Entrada de dados
numero = int(input("Digite um número: "))

# Processamento
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")