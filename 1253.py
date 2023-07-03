# Python code file

#cesar scypher
#
n = int(input())

for i in range(n):
    line = list(map(ord, input()))
    offset = int(input())

    for j in range(len(line)):
        line[j] = line[j] - offset
        if(line[j] >= 91):
            line[j] -= 26
        if(line[j] <= 64):
            line[j] += 26

    string = ''.join(map(chr, line))
    print(string)