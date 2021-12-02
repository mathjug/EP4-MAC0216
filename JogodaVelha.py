class TicTacToe:
    def __init__(self):
        self.board_pequeno = [0,[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
        self.board_grande = [[0,0,0],[0,0,0],[0,0,0]]
        self.ultima_jogada = [0,0,0,0,0,0,0,0,0,0]
        self.escolha_do_board = 1
        self.UltimateTicTacToeWins = 0
        self.jogador = 1
        jogar = 1
        jogar = int(input("\n                                           Sair(0) ou Jogar(1): "))
        if jogar == 1:
            self.menu()
        elif jogar == 0:
            print("\n                                                 Bye Bye...")
            exit()
        else: 
            print("\n                                            Sabe ler nao? Tchau!")
            exit()

    def menu(self):
            if self.ganhou(self.board_grande):
                if(self.jogador == 1): self.jogador = 2
                else: self.jogador = 1
                print("\n                                Parabens! O Jogador", self.jogador, "venceu o Ultimate TicTacToe!\n")
                exit()
            self.game()

    def board_reset(self):
        for i in range(3):
            for j in range(3):
                self.board_pequeno[self.escolha_do_board][i][j] = 0

    def jogada(self):
        self.linha  = int(input("\n                                 Digite a linha de sua jogada: "))
        self.coluna = int(input("\n                                 Digite a coluna de sua jogada: "))


    def game(self):
        jogadas=0
        
        while self.ganhou(self.board_grande) == 0:
            self.escolha_do_board = int(input("\n                                 Jogador " + str(self.jogador) + ". Digite em qual tabuleiro quer jogar: "))

            if self.escolha_do_board < 1 or self.escolha_do_board > 9 or self.board_grande[(self.escolha_do_board-1)//3][(self.escolha_do_board-1)%3] != 0:
                while self.escolha_do_board < 1 or self.escolha_do_board > 9 or self.board_grande[(self.escolha_do_board-1)//3][(self.escolha_do_board-1)%3] != 0:
                    self.escolha_do_board = int(input("\n                Tabuleiro ja vencido ou nao existe. Jogador " + str(self.jogador) + ". Digite em qual tabuleiro quer jogar: "))

            if self.ultima_jogada[self.escolha_do_board] == self.jogador:
                while self.ultima_jogada[self.escolha_do_board] == self.jogador:
                    self.escolha_do_board = int(input("\n                          Jogador " + str(self.jogador) + " teve sua ultima jogada aqui. Tente outro tabuleiro: "))

            print("\n                                 Tabuleiro", self.escolha_do_board, "do Ultimate TicTacToe. Vez do Jogador", self.jogador )
            print("\n                                               Tabuleiro", self.escolha_do_board)

            self.exibe(self.board_pequeno[self.escolha_do_board])
            self.jogada()

            if self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1] != 0:
                while self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1] != 0:
                    print("\n                                 Ja foi preenchido boroca, tente em outro lugar")
                    print("\n                                 Tabuleiro", self.escolha_do_board, "do Ultimate TicTacToe. Vez do Jogador", self.jogador)
                    print("\n                                               Tabuleiro", self.escolha_do_board)
                    self.exibe(self.board_pequeno[self.escolha_do_board])
                    self.jogada()

            if(self.jogador)==1:
                self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1]=1
                self.ultima_jogada[self.escolha_do_board] = 1
            else:
                self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1]=-1
                self.ultima_jogada[self.escolha_do_board] = 2
             
            if self.ganhou(self.board_pequeno[self.escolha_do_board]):
                print("\n                                 Tabuleiro", self.escolha_do_board, "do Ultimate TicTacToe")
                self.exibe(self.board_pequeno[self.escolha_do_board])
                print("\n                                 Parabens! Jogador",self.jogador,"ganhou depois de", jogadas+1,"rodadas no tabuleiro", self.escolha_do_board)
                qual_jogador = 1
                indice_x = 0
                indice_y = self.escolha_do_board - 1

                if(self.jogador) == 2: qual_jogador = -1

                if self.escolha_do_board > 2:
                    indice_x = indice_y//3
                    indice_y = indice_y%3

                self.board_grande[indice_x][indice_y] = qual_jogador
                print("\n                                         Tabuleiro Ultimate TicTacToe: ")
                self.exibe(self.board_grande)
                self.UltimateTicTacToeWins += 1
                if(self.jogador == 1): self.jogador = 2
                else: self.jogador = 1
                self.menu()

            print("\n                                               Tabuleiro", self.escolha_do_board)
            self.exibe(self.board_pequeno[self.escolha_do_board])
            if(self.jogador == 1): self.jogador = 2
            else: self.jogador = 1
            jogadas +=1
        
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
            self.exibe(self.board_pequeno[self.escolha_do_board])
            print("\n                                 Deu Velha! Tente de novo")
            if(self.jogador == 1): self.jogador = 2
            else: self.jogador = 1
            self.game()

        #verificar diagonais
        diagonal1 = board[0][0]+board[1][1]+board[2][2]
        diagonal2 = board[0][2]+board[1][1]+board[2][0]
        if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
            return 1

        return 0

    def exibe(self, board):
        for i in range(3):
            print("                                              |", end='')
            for j in range(3):
                if board[i][j] == 0:
                    print(" _ |", end='')
                elif board[i][j] == 1:
                    print(" X |", end='')
                elif board[i][j] == -1:
                    print(" O |", end='')
            print()
                
c = str(input("                                      Bem-Vindo ao Ultimate TicTacToe\n                                              (Aperte Enter)  "))
TicTacToe()
