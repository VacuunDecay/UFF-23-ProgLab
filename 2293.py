# Python code file

l, c = list(map(int, input().split()))

var = []
for i in range(l):
    line = list(map(int, input().split()))
    var.append(line)

lacum = [0]*l
cacum = [0]*c

i = 0
for i in range(c):
    for j in range(l):
        cacum[i] += var[j][i]
        lacum[j] += var[j][i]


max = 0
i = 0
for i in range(c):
    if(max < cacum[i]): max = cacum[i]

j = 0
for j in range(l):
    if(max < lacum[j]): max = lacum[j]

print(max)