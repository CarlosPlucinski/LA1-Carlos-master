# 11. Faça um script que receba valores inteiros e mostre na tela quantos desses valores recebidos estão no intervalo [10, 20] e quantos não estão. O programa irá parar de pedir números quando o usuário digitar um número negativo.
# Entrada:
# 10
# 12
# 21
# 32
# 14
# -1
# Saída:
# 3 números estão no intervalo
# 2 números estão fora do intervalo

contador_dentro = 0
contador_fora = 0
while True:
    valor = int(input("Digite um valor: "))

    if valor < 0:
        break

    if valor >= 10 and valor <= 20:
        contador_dentro += 1
    else:
        contador_fora += 1

    print(f"{contador_dentro} estão dentro do intervalo!")
    print(f"{contador_fora} estão fora do intervalo!")
    
