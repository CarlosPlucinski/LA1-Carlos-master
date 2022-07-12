#18. Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio R. A fórmula para calcular o volume é: (4/3) * pi * R^3. Considere (atribua) para pi o valor 3.14159.

r = float(input("Informe o valor de R para calcular a volume de uma esfera: "))
V = (4/3) * 3.14159 *(r*r*r)
print("O volume da esfera é de: ", V)