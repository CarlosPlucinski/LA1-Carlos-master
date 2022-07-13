# 13. Elabore um script que mostre na tela os 15 primeiros múltiplos de 7.
# Saída 7 14 21 28 35 42 49 56 63 70 77 84 91 98 105


numero = int(input(f"Digite um número: "))
valor = 7
for i in range(15):
    i += 1
    print(f"A lista dos numeros são {i * valor}")
