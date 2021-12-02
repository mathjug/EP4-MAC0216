def menu():
    c = 1
    c = int(input("\nSair(0) \n" + "Jogar(1) \n"))
    if c == 1:
        game()
    else:
        print("Bye Bye...")
        exit()

def board_reset(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = 0

def game():
    jogada=0

    board_reset(board)

    while ganhou() == 0:
        print("\nJogador", jogada%2 + 1)
        exibe()
        linha  = int(input("\nDigite a linha de sua jogada: "))
        coluna = int(input("Digite a coluna de sua jogada: "))

        if board[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                board[linha-1][coluna-1]=1
            else:
                board[linha-1][coluna-1]=-1
        else:
            print("\nJa foi preenchido boroca, tente em outro lugar")
            jogada -=1

        if ganhou():
            exibe()
            print("\nParabens! Jogador",jogada%2 + 1,"ganhou depois de", jogada+1,"rodadas")
            t = str(input("\nQuer jogar novamente? "))
            if t == "sim":
                menu()
            else: 
                print("\nObrigado por jogar!\n")
                exit()
        jogada +=1
    
def ganhou():
    #verificar linhas
    a = 0
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if board[i][0] == 0 or board[i][1] == 0 or board[i][2] == 0 : a = 1
        if soma==3 or soma ==-3:
            return 1

     #verificar colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if board[0][i] == 0 or board[1][i] == 0 or board[2][i] == 0 : a = 1
        if soma==3 or soma ==-3:
            return 1

    if a == 0 :
        t = str(input("\nDeu Velha! Quer jogar novamente? "))
        if t == "sim":
            menu()
        else: 
            print("\nObrigado por jogar!\n")
            exit()

    #verificar diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():
    for i in range(3):
        print("|", end='')
        for j in range(3):
            if board[i][j] == 0:
                print(" _ |", end='')
            elif board[i][j] == 1:
                print(" X |", end='')
            elif board[i][j] == -1:
                print(" O |", end='')

        print()
                
board=[[0,0,0],[0,0,0],[0,0,0]]

c = str(input("Quer jogar? "))
if c != "sim" and c != "nao":
    while c != "sim" and c != "nao":
        c = str(input("Quer jogar? "))
if c == "sim":
    menu()
