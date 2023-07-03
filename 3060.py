# Python code file

v = int(input())
p = int(input())

valor = v//p
valores = [valor]* p

resto = v%p

for i in range(resto):
    valores[i] += 1

for i in range(p):
    print(valores[i])