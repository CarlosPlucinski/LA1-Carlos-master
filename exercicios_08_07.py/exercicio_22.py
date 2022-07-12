# 22. Faça um programa que receba um número n e mostra na tela os n primeiros números bem como a informação se o número é ímpar ou par.
# Entrada:
# 5
# Saída:
# 1 - Ímpar
# 2 - Par
# 3 - Ímpar
# 4 - Par
# 5 - Ímpar

N = int(input("Digite o valor de N: "))

for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i} - Par")
    else:
        print(f"{i} - Ímpar")
        