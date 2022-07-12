#22. O tempo que um ônibus leva para chegar a um destino qualquer é 15 min. Receba a hora e o minuto de saída do ônibus e mostre na tela qual será o horário de chegada ao destino.


hora_saida = int(input("Digite a hora de saída: "))
minuto_saida = int(input("Digite a minuto de saída: "))

minuto_chegada = minuto_saida + 15

print(f"Saida: {hora_saida:02}:{minuto_saida} | Chegada: {hora_saida:02}:{minuto_chegada:02}")