class TicTacToe:
    def __init__(self):
        self.board_pequeno = [[0,0,0],[0,0,0],[0,0,0]]
        self.board_grande = [[0,0,0],[0,0,0],[0,0,0]]
        self.UltimateTicTacToeWins = 0
        jogar = 1
        jogar = int(input("\nSair(0) \n" + "Jogar(1) \n"))
        if jogar == 1:
            self.menu()
        else:
            print("Bye Bye...")
            exit()

    def menu(self):
        while(self.UltimateTicTacToeWins <= 9):
                if self.ganhou(self.board_grande):
                    print("\nParabens! O Jogador", self.jogador, "venceu o Ultimate TicTacToe!\n")
                    exit()
                self.game()

    def board_reset(self):
        for i in range(3):
            for j in range(3):
                self.board_pequeno[i][j] = 0

    def game(self):
        jogada=0

        self.board_reset()
        self.jogador = 2

        while self.ganhou(self.board_pequeno) == 0:
            if(self.jogador == 1): self.jogador = 2
            else: self.jogador = 1

            print("\nTabuleiro", self.UltimateTicTacToeWins+1, "do Ultimate TicTacToe\nVez do Jogador", self.jogador , "\n")

            self.exibe(self.board_pequeno)
            linha  = int(input("\nDigite a linha de sua jogada: "))
            coluna = int(input("Digite a coluna de sua jogada: "))

            if self.board_pequeno[linha-1][coluna-1] == 0:
                if(self.jogador)==1:
                    self.board_pequeno[linha-1][coluna-1]=1
                else:
                    self.board_pequeno[linha-1][coluna-1]=-1
            else:
                print("\nJa foi preenchido boroca, tente em outro lugar")
                jogada -=1

            if self.ganhou(self.board_pequeno):
                print("Tabuleiro", self.UltimateTicTacToeWins+1, "do Ultimate TicTacToe\n")
                self.exibe(self.board_pequeno)
                print("\nParabens! Jogador",self.jogador,"ganhou depois de", jogada+1,"rodadas")
                qual_jogador = 1
                indice_x = 0
                indice_y = self.UltimateTicTacToeWins
                if(self.jogador) == 2: qual_jogador = -1

                if self.UltimateTicTacToeWins > 2:
                    indice_x = indice_y/3
                    indice_y = indice_y%3

                self.board_grande[indice_x][indice_y] = qual_jogador
                print("\nTabuleiro Ultimate TicTacToe: \n")
                self.exibe(self.board_grande)
                self.UltimateTicTacToeWins = self.UltimateTicTacToeWins + 1
                self.menu()

            jogada +=1
        
    def ganhou(self, board):
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
                TicTacToe()
            else: 
                print("\nObrigado por jogar!\n")
                exit()

        #verificar diagonais
        diagonal1 = board[0][0]+board[1][1]+board[2][2]
        diagonal2 = board[0][2]+board[1][1]+board[2][0]
        if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
            return 1

        return 0

    def exibe(self, board):
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
                
c = str(input("Quer jogar? "))
if c != "sim" and c != "nao":
    while c != "sim" and c != "nao":
        c = str(input("Quer jogar? "))
if c == "sim":
    TicTacToe()
