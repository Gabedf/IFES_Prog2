def troca_linhas(mat,la,lb):
  aux = 0

  for j in range(len(mat[la])):
    aux = mat[la][j]
    mat[la][j] = mat[lb][j]
    mat[lb][j] = aux

def print_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%4d" % mat[i][j], end="")
        print()

def main():
    import LstGenerator as l

    m = l.gerador()
    print_mat(m)
    troca_linhas(m,0,2)
    print()
    print_mat(m)

main()