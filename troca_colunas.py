def colunas(mat, ca, cb):
    aux = 0
    for i in range(len(mat)):
        aux = mat[i][ca]
        mat[i][ca] = mat[i][cb]
        mat[i][cb] = aux

def print_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%4d" % mat[i][j], end="")
        print()

def main():
    import LstGenerator as l

    m = l.gerador()
    print_mat(m)
    colunas(m,0,2)
    print()
    print_mat(m)

main()