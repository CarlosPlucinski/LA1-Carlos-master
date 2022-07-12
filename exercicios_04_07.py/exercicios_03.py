# 3. Mostre na tela um menu para um sistema de cadastro de funcionários. O menu deve estar no seguinte formato:

# Cadastro de funcionários

# a) Cadastrar funcionários
# b) Listar funcionários
# c) Editar funcionário
# d) Remover funcionário
# e) Sair

# Digite a opção desejada:

cadastro = input("""
Cadastro de funcionários

a) Cadastrar funcionários:
b) Listar funcionários:
c) Editar funcionário:
d) Remover funcionário:
e) Sair:

Digite a opção desejada:""")
print(f"A opção escolhido foi: {cadastro}")