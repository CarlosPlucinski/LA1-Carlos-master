# 07. Escreva um script que receba um número, se esse número estiver entre 20 e 90 mostre na tela "O número está na faixa entre 20 e 90" senão mostre "O número está fora da faixa".

# Exemplo 01
# Entrada:
# 21
# Saída:
# O número está na faixa entre 20 e 90

# Exemplo 02
# Entrada:
# 20
# Saída:
# O número está fora da faixa

# Exemplo 03
# Entrada:
# 90
# Saída:
# O número está fora da faixa

numero = 90

if numero > 20 and numero < 90:
    print("O número está na faixa entre 20 e 90")
else:
    print("O número está fora da faixa")