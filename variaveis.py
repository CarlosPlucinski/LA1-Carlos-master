"""
Regras de nomenclatura das variáveis:
    - Não pode iniciar com símbolos (com exceção do _)  ou números.
    - Cada palavra deve ser separada por _.
    - Os nomes das variáveis devem ser descritivos.
"""

nome_completo = "Carlos Plucinski" # str
print("O meu nome é", nome_completo) # Carlos Plucinski
print(f"O meu nome é {nome_completo}!E eu estou triste porque é segunda!") # Carlos Plucinski

vazio = None # NoneTrype
numero_inteiro = 250 #int
numero_decimal = 20.2 #float
presente = True #bool

numero_inteiro = 255
numero_decimal = "20.2"

# print(10 + numero_decimal)
# print(10 * numero_decimal)
# print(10 / numero decimal)
print(10.2 + 2) 

print(vazio) # None
print(numero_inteiro) # 255
print(numero_decimal) # '20.2'
print(presente) #True

print(type(nome_completo)) # <class 'str'>
print(type(vazio)) # <class 'NoneType'>
print(type(numero_inteiro)) # <class 'int'>
print(type(numero_decimal)) # <class 'str'>

# Criar múltiplas variáveis ao mesmo tempo
a, b, c = 1, 2, 3

# Trocar valores entre variáveis
a = 10 # a = 10, b = None, aux = None
b = 5 # a = 10, b = 5, aux = None
aux = a # a = 10, b = 5, aux = 10
a = b # a = 5, b = 5, aux = 10 
b = aux # a = 5, b = 10, aux = 10
print(a, b)

c: int = 10 # Type hinting
d = 5
c, d = d, c
print(c, d)

valor_com_muitas_casas_decimais = 10.1237918273918273814
print(f"O valor formatado é: {valor_com_muitas_casas_decimais:.2f}")
