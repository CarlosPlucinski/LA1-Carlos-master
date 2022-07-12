#15. Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, mostrar na tela os valores que ficaram armazenados nas variáveis.

valor_A = 10
valor_B = 20
valor_C = 0

valor_C = valor_A
valor_A = valor_B
valor_B = valor_C

print("A = ", valor_A)
print("B = ", valor_B)