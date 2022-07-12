# range1 = range(10)
# print(type(range1))

# for i in range(0, 10, 4):
#     print(f'I vale: {i}')

# Continuar pedindo números enquanto 0 não for digitado e ao final mostrar a soma dos números digitados

# soma = 0
# while True:
#     valor_digitado = int(input("Digite qualquer coisa ou 0 para sair: "))

#     if not valor_digitado:
#         break

#     soma += valor_digitado

# print(f"A soma dos números é {soma}")
# print("Finalizou o programa")

# for i in range (10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(2):
#     for j in range(2):
#         print(i + j)


'''
Em python o laço de repetição for requer a utilização de um Iterable.
Um Iterable é uma coleção que possui vários valores.
O Iterable que vamos utilizar para construir o nosso laço de repetição é
o range().
A função range(x) cria uma sequência de números de acordo com o valor x.
Portanto se utilizarmos o comando range(10), teremos a seguinte coleção:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -> Sempre começa em 0.
'''

for i in range(10):
    print(f"O laço está repetindo pela {i + 1} vez")

# A função range aceita o valor inicial e o passo:
# range(valor_inicial, valor_final, passo)
for i in range(1, 10, 2):
    print(i)

# Se quisermos exibir o resultado na mesma linha:
for i in range(10):
    print(i, end=" ")