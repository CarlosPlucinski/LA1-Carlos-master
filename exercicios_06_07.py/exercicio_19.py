# 19. Para doar sangue é necessário ter entre 18 e 67 anos. Faça um script que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
# Use o operador lógicos OU (or).

idade = int(input("Informe sua idade: "))
if idade > 67 or idade < 18:
    print("Você não pode doar sangue!")
else:
    print("Você pode doar sangue!")