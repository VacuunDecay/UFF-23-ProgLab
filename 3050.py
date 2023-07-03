# Python code file

n = int(input())
vet = list(map(int, input().split()))

max = 0
for i in range(n):
    for j in range(i+1, n):
        chao = j - i
        dist = chao + vet[i]+ vet[j]
        if(dist > max):
            max = dist

print(max)