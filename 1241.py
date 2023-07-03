n = int(input())

for i in range(n):
    line = list(map(str, input().split()))
    line[0] = line[0][-len(line[1]):]

    if line[0] == line[1]:
        print("encaixa")
    else:
        print("nao encaixa")
