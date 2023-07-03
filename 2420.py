# Python code file

n = int(input())
a = list(map(int, input().split()))

soma = 0

for i in range(n):
    soma += a[i]

pais1 = soma
pais2 = 0
divisao = 0

for i in range(n):
    if(pais1 == pais2):
        print(divisao)
        break
    pais1 -= a[i]
    pais2 += a[i]
    divisao += 1