# 18. Faça um script que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
if n1 > n2 and n2 > n3:
    print(f"A ordem dos números são: {n1} {n2} {n3}")
elif n2 > n1 and n1 > n3:
    print(f"A ordem dos números são: {n2} {n1} {n3}")
# elif n3 > n1 and n1 > n2:
#     print(f"A ordem dos números são: {n3} {n1} {n2}")




