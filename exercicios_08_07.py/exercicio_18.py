# 18. Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 4 alunos.
# a) a média de cada aluno será fornecida pelo usuário.
# b) a tabela de conceitos se encontra abaixo:

# ____________________________
# | Nota	      | Conceito |
# | de 0.0 à 4.9  | D        |
# | de 5.0 à 6.9  | C        |
# | de 7.0 à 8.9  | B        |
# | de 9.0 à 10.0 | A        |
# |_______________|__________|

for i in range(4):
    media = float(input("Digite a média do aluno: "))

    if media < 0:
        print("Média inválida")
    elif media < 5:
        print("D")
    elif media < 7:
        print("C")
    elif media < 9:
        print("B")
    else:
        print("A")