tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4 ,0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def mostra_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tabuleiro[i][j])
            else:
                print(str(tabuleiro[i][j]) + " ", end="")

def achar_vazio(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 0:
                return (i, j)

    return None

def valor_valido(posicao, valor, tabuleiro):
    #linha
    for i in range(len(tabuleiro)):
        if tabuleiro[posicao[0]][i] == valor and posicao[1] != i:
            return False

    #coluna
    for i in range(len(tabuleiro)):
        if tabuleiro[i][posicao[1]] == valor and posicao[0] != i:
            return False
    
    #caixa
    caixa_x = posicao[0] // 3
    caixa_y = posicao[1] // 3

    for i in range(caixa_x * 3, caixa_x * 3 + 3):
        for j in range(caixa_y * 3, caixa_y * 3 + 3):
            if tabuleiro[i][j] == valor and (i, j) != posicao:
                return False

    return True

def solucao(tabuleiro):
    vazio = achar_vazio(tabuleiro)
    if not vazio:
        return True
    else:
        linha, coluna = vazio

    for i in range(1, 10):
        if valor_valido((linha, coluna), i, tabuleiro):
            tabuleiro[linha][coluna] = i

            if solucao(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0

    return False
        
mostra_tabuleiro(tabuleiro)
print("\n")
solucao(tabuleiro)
mostra_tabuleiro(tabuleiro)