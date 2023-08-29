import random

def gerador():
    lista = []

    linha = random.randint(1, 10)

    for i in range(linha):
        x = []
        for j in range(linha):
            y = random.randint(1, 10)
            x.append(y)
        lista.append(x)
    
    return lista

def print_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%4d" % mat[i][j], end="")
        print()

