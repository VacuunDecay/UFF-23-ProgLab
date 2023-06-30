n = int(input())

out = ""

for i in range(n):
    line = input()
    if(len(line) != 0 and line[0] != ' '):
        out += line[0]
    for j in range(len(line)-1):
        if(line[j] == ' ' and line[j+1] != ' '):
            out += line[j+1]
    print(out)
    out = ""