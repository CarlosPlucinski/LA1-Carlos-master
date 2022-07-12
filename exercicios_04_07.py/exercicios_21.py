# 21. Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
# Entrada:
# João
# 500
# 1230.3
# Saída:
# Total = R$ 684.54


nome = input("Informe seu nome: ")
salario_fixo = float(input("Informe seu salário: R$ "))
vendas = float(input("Informe o valor total de vendas efetuadas no mês: R$ "))

comissao = (vendas * 15)/100
salario_final = salario_fixo + comissao

print("Nome: ", nome)
print("Total de vendas: R$ ", vendas)
print("Salário : R$ {:.2f}".format(salario_final))