# 09. Escreva um script que receba três valores A, B, C. Faça as comparações necessárias para exibir na tela o maior valor entre os três.

# Exemplo 01
# Entrada:
# 10
# 12
# 2
# Saída:
# O maior número é 12

# Exemplo 02
# Entrada:
# 12
# 2
# 10
# Saída:
# O maior número é 12

# Exemplo 03
# Entrada:
# 2
# 10
# 12
# Saída:
# O maior número é 12

valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor2: "))
valor3 = int(input("Digite o valor3: "))
if valor1 > valor2 and valor1 > valor3:
    print(f"O maior número é {valor1}! ")
elif valor2 > valor3:
    print(f"O maior número é {valor2}! ")
else:
    print(f"O maior número é {valor3}! ")



