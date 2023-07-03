# Python code file

n , c = list(map(int, input().split()))
vet = list(map(int, input().split()))

pos = 0
luc = [0]*len(vet)

max = 0
for i in range(n):
    max = vet[i]
    for j in range(i, n):
        if(max < vet[j]): max = vet[j]
        if(max > vet[j]): 
            luc = max - vet[i]
max = 0

for i in range(len(luc)):
    luc[i] -= c
    if(luc[i] >= 0):
        max += luc[i]

print(max)