# 19. Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero. Entrada:
# 0012021
# 10
# 8
# 9
# 0022021
# 10
# 10
# 10
# 0
# Saída:
# A média do aluno com a matrícula 0012021 é 9.00
# A média do aluno com a matrícula 0022021 é 10.00

while True:
    matricula = int(input("Digite a matrícula do aluno: "))

    if matricula == 0:
        break

    soma = 0
    for i in range(3):
        nota = float(input(f"Digite a {i + 1}° nota do alunio: "))
        soma += nota

    media = soma / 3
    
    print(f"A média do aluno com a matrícula {matricula} é {media}")