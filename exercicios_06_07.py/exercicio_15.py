# 15. Leia o salario de um trabalhador e o valor da prestação de um empréstimo. Se a prestaçao for maior que 20% do salário imprima: “empréstimo não concedido”, caso contrario imprima: “empréstimo concedido”.

salario = float(input("Informe o seu salário: "))
emprestimo = float(input("Informe o valor da prestação de um empréstimo: "))
s1 = (salario*20)/100

if emprestimo > s1:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")

