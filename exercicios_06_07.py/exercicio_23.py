# 23. Escreva um algoritmo que peça o salário de uma pessoa e imprima o salário líquido, segunda a tabela a seguir:
# __________________________________________________________
# |Menor ou igual a R$ 600.00                       |Isento|
# |Maior que R$600.00 e menor ou igual a R$ 1200.00	|20%   |
# |Maior que R$1200.00 e menor ou igual a R$2000.00	|25%   |
# |Maior que R$ 2000.00	                            |30%   |
# |_________________________________________________|______|




# Tente não utilizar o operador *and*

salario = float(input("Informe o seu salário: "))
if salario <= 600:
    print("Salário líquido:", salario )
elif salario <= 1200 or salario > 600:
    print("Salário líquido", salario-(salario * 0.20))
elif salario <= 2000 or salario > 1200:
    print("Salário líquido", salario-(salario * 0.25))
elif salario > 2000:
    print("Salário líquido", salario-(salario * 0.3))