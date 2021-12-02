class TicTacToe:
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        c = 1
        c = int(input("\nSair(0) \n" + "Jogar(1) \n"))
        if c == 1:
            self.game()
        else:
            print("Bye Bye...")
            exit()

    def board_reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0

    def game(self):
        jogada=0

        self.board_reset()

        while self.ganhou() == 0:
            print("\nJogador", jogada%2 + 1)
            self.exibe()
            linha  = int(input("\nDigite a linha de sua jogada: "))
            coluna = int(input("Digite a coluna de sua jogada: "))

            if self.board[linha-1][coluna-1] == 0:
                if(jogada%2+1)==1:
                    self.board[linha-1][coluna-1]=1
                else:
                    self.board[linha-1][coluna-1]=-1
            else:
                print("\nJa foi preenchido boroca, tente em outro lugar")
                jogada -=1

            if self.ganhou():
                self.exibe()
                print("\nParabens! Jogador",jogada%2 + 1,"ganhou depois de", jogada+1,"rodadas")
                t = str(input("\nQuer jogar novamente? "))
                if t == "sim":
                    TicTacToe()
                else: 
                    print("\nObrigado por jogar!\n")
                    exit()
            jogada +=1
        
    def ganhou(self):
        #verificar linhas
        a = 0
        for i in range(3):
            soma = self.board[i][0]+self.board[i][1]+self.board[i][2]
            if self.board[i][0] == 0 or self.board[i][1] == 0 or self.board[i][2] == 0 : a = 1
            if soma==3 or soma ==-3:
                return 1

        #verificar colunas
        for i in range(3):
            soma = self.board[0][i]+self.board[1][i]+self.board[2][i]
            if self.board[0][i] == 0 or self.board[1][i] == 0 or self.board[2][i] == 0 : a = 1
            if soma==3 or soma ==-3:
                return 1

        if a == 0 :
            t = str(input("\nDeu Velha! Quer jogar novamente? "))
            if t == "sim":
                TicTacToe()
            else: 
                print("\nObrigado por jogar!\n")
                exit()

        #verificar diagonais
        diagonal1 = self.board[0][0]+self.board[1][1]+self.board[2][2]
        diagonal2 = self.board[0][2]+self.board[1][1]+self.board[2][0]
        if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
            return 1

        return 0

    def exibe(self):
        for i in range(3):
            print("|", end='')
            for j in range(3):
                if self.board[i][j] == 0:
                    print(" _ |", end='')
                elif self.board[i][j] == 1:
                    print(" X |", end='')
                elif self.board[i][j] == -1:
                    print(" O |", end='')
            print()
                
c = str(input("Quer jogar? "))
if c != "sim" and c != "nao":
    while c != "sim" and c != "nao":
        c = str(input("Quer jogar? "))
if c == "sim":
    TicTacToe()
