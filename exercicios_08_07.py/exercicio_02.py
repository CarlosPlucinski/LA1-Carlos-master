# 02. Elabore três scripts que mostrem a mensagem "Estou aparecendo pela <numero_de_vezes> na tela!" 10 vezes. Substitua <numero_de_vezes> pela iteração atual do loop. Utilize uma estrutura de repetição diferente em cada um dos scripts (for e while).

for i in range(10):
    print(f"Estou aparecendo pela {i + 1} na tela!")        # FOR


i: int = 0
while i < 10:
    print(f"Estou aparecendo pela {i + 1} na tela!")        # WHILE
    i += 1


