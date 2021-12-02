import random

class TicTacToe:
    def __init__(self):
        jogar = 1
        jogar = int(input("\n                                           Sair(0) ou Jogar(1): "))

        if jogar == 1:
            self.board_pequeno = [0,[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
            self.board_grande = [[0,0,0],[0,0,0],[0,0,0]]
            self.escolha_do_board = 1
            self.UltimateTicTacToeWins = 0
            self.jogador = 1
            a = int(input("                      Escolha o tipo do Jogador 1: (0) Humano (1) Aleatorio (2) Come-cru "))
            b = int(input("                      Escolha o tipo do Jogador 2: (0) Humano (1) Aleatorio (2) Come-cru "))
            self.tipo_jogadores = [0,a,b]
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
                print("\n                             Parabens! O Jogador", self.jogador, "venceu o Ultimate TicTacToe!\n")
                exit()
            self.game()

    def board_reset(self, board):
        for i in range(3):
            for j in range(3):
                board[i][j] = 0

    def jogada(self):

        if self.tipo_jogadores[self.jogador] == 0: self.jogada_humano()
        elif self.tipo_jogadores[self.jogador] == 1: self.jogada_random()
        else: self.jogada_come_cru()

    def jogada_humano(self):
        self.linha  = int(input("\n                                 Digite a linha de sua jogada: "))
        while self.linha < 1 or self.linha > 3:
            self.linha  = int(input("\n                                 Linha nao existe. Digite a linha de sua jogada: "))
        self.coluna = int(input("\n                                 Digite a coluna de sua jogada: "))
        while self.coluna < 1 or self.coluna > 3:
            self.coluna  = int(input("\n                                Coluna nao existe. Digite a coluna de sua jogada: "))

    def jogada_random(self):
        self.linha = random.randint(1,3)
        self.coluna = random.randint(1,3)

    def jogada_come_cru(self):
        for i in range(3):
            for j in range(3):
                if self.board_pequeno[self.escolha_do_board][i][j] == 0: 
                    self.linha = i
                    self.coluna = j

    def game(self):
        
        while self.ganhou(self.board_grande) == 0:
            if(self.tipo_jogadores[self.jogador] == 0 or self.tipo_jogadores[self.jogador] == 2):
                self.escolha_do_board = int(input("\n                                 Jogador " + str(self.jogador) + ". Digite em qual tabuleiro quer jogar: "))
            else :
                self.escolha_do_board = random.randint(1,9)
                while self.board_grande[(self.escolha_do_board-1)//3][(self.escolha_do_board-1)%3] != 0:
                    self.escolha_do_board = random.randint(1,9)

            while self.escolha_do_board < 1 or self.escolha_do_board > 9 or self.board_grande[(self.escolha_do_board-1)//3][(self.escolha_do_board-1)%3] != 0:
                self.escolha_do_board = int(input("\n                Tabuleiro " + str(self.escolha_do_board) + " ja vencido ou nao existe. Jogador " + str(self.jogador) + ". Digite em qual tabuleiro quer jogar: "))

            print("\n                               Tabuleiro", self.escolha_do_board, "do Ultimate TicTacToe. Vez do Jogador", self.jogador )
            print("\n                                               Tabuleiro", self.escolha_do_board)

            self.exibe(self.board_pequeno[self.escolha_do_board])
            self.jogada()

            while self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1] != 0:
                if(self.tipo_jogadores[self.jogador] == 0):
                    print("\n                               Ja foi preenchido boroca, tente em outro lugar")
                    print("\n                               Tabuleiro", self.escolha_do_board, "do Ultimate TicTacToe. Vez do Jogador", self.jogador)
                    print("\n                                               Tabuleiro", self.escolha_do_board)
                    self.exibe(self.board_pequeno[self.escolha_do_board])
                self.jogada()

            if(self.jogador)==1:
                self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1]=1
            else:
                self.board_pequeno[self.escolha_do_board][self.linha-1][self.coluna-1]=-1
             
            if self.ganhou(self.board_pequeno[self.escolha_do_board]):
                print("\n                                               Tabuleiro", self.escolha_do_board)
                self.exibe(self.board_pequeno[self.escolha_do_board])
                print("\n                                   Parabens! Jogador",self.jogador,"ganhou o tabuleiro", self.escolha_do_board)
                qual_jogador = 1
                indice_x = 0
                indice_y = self.escolha_do_board - 1

                if(self.jogador) == 2: qual_jogador = -1

                if self.escolha_do_board > 2:
                    indice_x = indice_y//3
                    indice_y = indice_y%3

                self.board_grande[indice_x][indice_y] = qual_jogador
                print("\n                                       Tabuleiro Ultimate TicTacToe ")
                self.exibe(self.board_grande)
                self.UltimateTicTacToeWins += 1
                if(self.jogador == 1): self.jogador = 2
                else: self.jogador = 1
                self.menu()

            print("\n                                               Tabuleiro", self.escolha_do_board)
            self.exibe(self.board_pequeno[self.escolha_do_board])
            if(self.jogador == 1): self.jogador = 2
            else: self.jogador = 1
        
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
            if(self.UltimateTicTacToeWins == 9):
                print("\n                              Ninguem ganhou o Ultimate TicTacToe, tente novamente")  
                exit()
            print("\n                                               Tabuleiro", self.escolha_do_board)
            self.exibe(self.board_pequeno[self.escolha_do_board])
            print("\n                                         Deu Velha! Tente de novo")
            self.board_reset(self.board_pequeno[self.escolha_do_board])
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
