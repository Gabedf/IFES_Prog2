def gera_matriz(linha, coluna, min, max):
    # Gera uma matriz (listas de listas) com linha, coluna e número mínimo e máximo passados como parâmetros
    import random
    lista = []

    for i in range(linha):
        x = []
        for j in range(coluna):
            y = random.randint(min, max)
            x.append(y)
        lista.append(x)
    """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print("%4d" % lista[i][j], end="")
        print()
    """
    return lista

def salva_matriz(matriz, nomeArquivo):
    # Cria um arquivo 'txt' com os elementos da matriz, passados linha a linha
    nomeArquivo = nomeArquivo + '.txt'
    arq = open(nomeArquivo, "wt")

    for i in range(len(matriz)):
        x = str(matriz[i][0]) + ',' + str(matriz[i][1]) + ',' +  str(matriz[i][2]) + ',' + str(matriz[i][3]) + '\n'
        arq.writelines(x)
    
    arq.close()

def main():
    
    nome = input("Nome do arquivo texto a ser criado: ")
    linha = int(input('Número de linhas da matriz: '))
    coluna = int(input('Número colunas da matriz: '))
    min = int(input('Número mínimo do elemento: '))
    max = int(input('Número máximo do elemento: '))
    matriz = gera_matriz(linha, coluna, min, max)

    salva_matriz(matriz, nome)

    print('PROGRAMA EXECUTADO COM SUCESSO')

main()