def print_mat(mat):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("%4d" % mat[i][j], end="")
        print()

def main():
    import LstGenerator as l

    m = l.gerador()
    print_mat(m)

main()

