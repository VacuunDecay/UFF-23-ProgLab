# Python code file

R = int(input(), 16)
G = int(input(), 16)
B = int(input(), 16)

g = R//G
g = g**2

b = G//B
b = b**2 * g

print(hex(1+g+b)[2:])