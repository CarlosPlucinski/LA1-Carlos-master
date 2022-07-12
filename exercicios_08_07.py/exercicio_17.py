# 17. Faça um programa que simule a urna eleitoral. Apresente um menu com as seguintes informações para o usuário:
# 1 - José Bolinha
# 2 - Maria Nascimento
# 3 - João da Silva
# 4 - Voto nulo
# 5 - Voto em branco
# Após isso, leia o voto digitado pelo usuário até que ele digite o valor 0. Ao final mostre:

# Total de votos para cada candidato;
# Total de votos nulos;
# Total de votos em branco.
# Entrada:
# 1
# 1
# 2
# 3
# 3
# 4
# 5
# 0

# Saída:
# Total de Votos
# José Bolinha: 2 voto(s)
# Maria Nascimento: 1 voto(s)
# João da Silva: 2 voto(s)
# Votos nulos: 1 voto(s)
# Votos em branco: 1 voto(s)

jose = 0
maria = 0
joao = 0
nulo = 0
branco = 0

while True:
    voto = input("""
1 - José Bolinha
2 - Maria Nascimento
3 - João da Silva
4 - Voto nulo
5 - Voto em branco
Digite o seu voto: """)
    if voto == "0": 
        break

    if voto == "1":
        jose += 1
    elif voto == "2":
        maria += 1
    elif voto == "3":
        joao += 1
    elif voto == "4":
        nulo += 1
    elif voto == "5":
        branco += 1
    else:
        print("Valor inválido")

print(f"""
# Total de Votos
# José Bolinha: {jose} voto(s)
# Maria Nascimento: {maria} voto(s)
# João da Silva: {joao} voto(s)
# Votos nulos: {nulo} voto(s)
# Votos em branco: {branco} voto(s)""")


