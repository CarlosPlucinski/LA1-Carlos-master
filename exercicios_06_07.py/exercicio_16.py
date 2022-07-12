# 16. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, a vitória do primeiro time ou do segundo time.

time1 = int(input("Digite a quantidade de gol do time1: "))
print(time1)

time2 = int(input("Digite a quantidade de gol do time2: "))
print(time2)
if time1 > time2:
    print(f"O time vencedor foi: {time1} ")
elif time1 < time2:
    print(f"O time vencedor foi: {time2} ")
else:
    print(f"A partida ficou empatada! ")
    
