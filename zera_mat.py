def zera_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = 0

def print_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%4d" % mat[i][j], end="")
        print()
        
def main():
    import LstGenerator as l

    m = l.gerador()
    print_mat(m)
    zera_mat(m)
    print()
    print_mat(m)

main()