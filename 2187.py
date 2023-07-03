# Python code file

cedulas = [50, 10, 5, 1]
saida = [0, 0, 0, 0]
inp = 1
j = 0
while(1):
    j+= 1
    inp = int(input())
    if(inp == 0): break
    for i in range(4):
        saida[i] = inp//cedulas[i]
        inp = inp%cedulas[i]
    print(f"Teste {j}") 
    print(f"{saida[0]} {saida[1]} {saida[2]} {saida[3]}")
    print() 
