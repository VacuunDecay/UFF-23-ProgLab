# Python code file

def move1(vet):
    aux = vet[0]
    vet[0] = vet[1]
    vet[1] = aux
    return vet

def move2(vet):
    aux = vet[1]
    vet[1] = vet[2]
    vet[2] = aux
    return vet
    
def move3(vet):
    aux = vet[0]
    vet[0] = vet[2]
    vet[2] = aux
    return vet

n = int(input())
vec = [0, 0, 0]

inp = str(input())
if(inp == "A"):
    vec[0] = 1
elif(inp == "B"):
    vec[1] = 1
elif(inp == "C"):
    vec[2] = 1

for i in range(n):
    inp = int(input())
    if(inp == 1): move1(vec)
    elif(inp == 2): move2(vec)
    elif(inp == 3): move3(vec)

if(vec[0] == 1): print("A")
elif(vec[1] == 1): print("B")
elif(vec[2] == 1): print("C")