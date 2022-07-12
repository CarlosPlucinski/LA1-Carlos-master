verdadeiro = True
falso = False

print(bool(1)) # True
print(bool(0)) # O 0 sempre vai ser falso
print(bool(10)) # True
print(bool(-10)) # True
print(bool(10.23)) # True
print(bool(0.23)) # True
print(bool(0.0)) # False
print(bool("a")) # True
print(bool("0")) # True pq é uma string
print(bool("")) # False string vázia é sempre falso

valor = "" # False

if not valor: # True
    print("Você nao digitou um valor")

if valor == "":
    print("Você não digitou um valor")


