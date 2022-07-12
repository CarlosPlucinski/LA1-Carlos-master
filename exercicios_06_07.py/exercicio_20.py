# 20. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se for 1, segunda-feira se for 2, e assim por diante.

numero = int(input("Informe um número entre 1 e 7: "))
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-Feira")
elif numero == 3:
    print("Terça-Feira")
elif numero == 4:
    print("Quarta-Feira")
elif numero == 5:
    print("Quinta-Feira")
elif numero == 6:
    print("Sexta-Feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido")


