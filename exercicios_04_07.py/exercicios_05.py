#5. Crie um script que receba o nome, idade, peso, altura e telefone de vocês e mostra essas informações na tela do console. Nome: <nome>
# Idade: <idade>
# Peso: <peso>
# Altura: <altura>
# Telefone: <telefone>

nome = input("Qual é o seu nome?: ")
idade = input("Qual é a sua idade?: ")
peso = input("Qual é o seu peso?: ")
altura = input("Qual é a sua altura?: ")
telefone = input("Qual é o seu telefone?: ")

print(f"""
nome: {nome}
idade: {idade}
peso: {peso}
altura: {altura}
telefone: {telefone}
""")