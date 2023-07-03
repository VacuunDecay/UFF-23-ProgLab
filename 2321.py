def retangulos_colidem(p1, p2, p3, p4):
    # Verificar colisão ao longo do eixo x
    if p2[0] < p3[0] or p1[0] > p4[0]:
        return False

    # Verificar colisão ao longo do eixo y
    if p2[1] < p3[1] or p1[1] > p4[1]:
        return False

    return True

# Leitura das coordenadas
p1x, p1y, p2x, p2y = map(int, input().split())
p3x, p3y, p4x, p4y = map(int, input().split())

# Armazenar coordenadas em tuplas
p1 = (p1x, p1y)
p2 = (p2x, p2y)
p3 = (p3x, p3y)
p4 = (p4x, p4y)

# Verificar se os retângulos colidem
colisao = retangulos_colidem(p1, p2, p3, p4)

# Impressão do resultado
if colisao:
    print("1")
else:
    print("0")
