# 17. Desenvolva um programa que receba do usuário a sua idade e informe a situação de voto dele ("Não pode votar", "Voto opcional", "Voto obrigatório"). Voto Opcional:

# * maiores de 16 anos e menores de 18 anos;
# * maiores de 70 anos; Voto obrigatório:
# * maior que 18 e menor que 70 Não pode votar:
# * menor de 16 anos

usuario = int(input("Informe a sua idade: "))
if usuario >= 16 and usuario < 18:
    print("Voto opcional")
elif usuario >= 70:
    print("Voto opcional")
elif usuario > 18 and usuario < 70:
    print("Voto obrigatório")
elif usuario < 16:
    print("Não pode votar")