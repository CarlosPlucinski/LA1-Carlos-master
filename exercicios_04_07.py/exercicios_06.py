# 6.Armazene em variáveis as seguintes informações sobre o último livro que você leu:

# Título
# Edição
# Autor
# Data de publicação
# Após isso mostre na tela essas informações no seguinte formato:
# Título: <titulo>
# Edição: <edição>
# Autor: <autor>
# Data de publicação: Data de publicação

titulo = input("Título do livro: ")
edicao = input("Edição: ")
autor = input("Autor: ")
data_de_publicacao = input("Data de publicação: ")

print(f"""
Titulo: {titulo}
Edição: {edicao}
Autor: {autor}
Data de publicação: {data_de_publicacao}
""")