'''
EP4 MAC0216
INTEGRANTES: Matheus Sanches Jurgensen (12542199), Caio Rodrigues Gama (12543381)
DATA: 10/12/2021

EXTRAS IMPLEMENTADOS:
'''

import random

class Tabuleiro:
    '''
    Abstração para um tabuleiro. É uma "superclasse" de MacroTabuleiro e de MicroTabuleiro.
    '''
    def alteraTabuleiro(self, linha, coluna, elemento):
        '''
        Recebendo uma linha, uma coluna e um elemento, atribui o elemento à posição do tabuleiro
        dada pela linha e pela coluna.
        '''
        self.tabuleiro[linha][coluna] = elemento

    def chegouAoFim(self):
        '''
        Retorna 2 caso o tabuleiro analisado tiver sido finalizado com o jogador2 vencedor.
        Retorna 1 caso o tabuleiro analisado tiver sido finalizado com o jogador1 vencedor.
        Retorna 0 caso o tabuleiro analisado não tiver sido finalizado.
        Retorna -1 caso o tabuleiro analisado tiver sido finalizado sem um jogador vencedor (velha).
        '''
        velha = True
        # verificar linhas
        for linha in range(3):
            if (type(self.tabuleiro[linha][0]) == str) and (type(self.tabuleiro[linha][1]) == str) and (type(self.tabuleiro[linha][2]) == str):
                soma = ""
                for j in range(3):
                    if self.tabuleiro[linha][j] == " ":
                        velha = False
                    soma += self.tabuleiro[linha][j]
                if (soma == "OOO"):
                    return 1
                elif (soma == "XXX"):
                    return 2
            else:
                velha = False

        # verificar colunas
        for coluna in range(3):
            if (type(self.tabuleiro[0][coluna]) == str) and (type(self.tabuleiro[1][coluna]) == str) and (type(self.tabuleiro[2][coluna]) == str):
                soma = ""
                for i in range(3):
                    if self.tabuleiro[i][coluna] == " ":
                        velha = False
                    soma += self.tabuleiro[i][coluna]
                if (soma == "OOO"):
                    return 1
                elif (soma == "XXX"):
                    return 2
            else:
                velha = False

        # verificar diagonais
        if (type(self.tabuleiro[0][0]) == str) and (type(self.tabuleiro[1][1]) == str) and (type(self.tabuleiro[2][2]) == str):
            soma = self.tabuleiro[0][0] + self.tabuleiro[1][1] + self.tabuleiro[2][2]
            if (soma == "OOO"):
                return 1
            elif (soma == "XXX"):
                return 2
        if (type(self.tabuleiro[0][2]) == str) and (type(self.tabuleiro[1][1]) == str) and (type(self.tabuleiro[2][0]) == str):
            soma = self.tabuleiro[0][2] + self.tabuleiro[1][1] + self.tabuleiro[2][0]
            if (soma == "OOO"):
                return 1
            elif (soma == "XXX"):
                return 2

        if velha:
            return -1
        
        return 0 # tabuleiro ainda não finalizado

class MacroTabuleiro(Tabuleiro):
    '''
    Abstração para um macro tabuleiro. É um Tabuleiro cujas casas são compostas por outros (micro) tabuleiros.
    Em geral, o usuário se refere às casas do macro tabuleiro de 1 a 9, da seguinte forma:

     1 | 2 | 3 
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

    No entanto, para facilitar a implementação, os métodos se referem às casas do macro tabuleiro de 0 a 8:
     0 | 1 | 2 
    -----------
     3 | 4 | 5
    -----------
     6 | 7 | 8
    '''
    def __init__(self):
        Tabuleiro.__init__(self)
        tabuleiro1 = MicroTabuleiro()
        tabuleiro2 = MicroTabuleiro()
        tabuleiro3 = MicroTabuleiro()
        tabuleiro4 = MicroTabuleiro()
        tabuleiro5 = MicroTabuleiro()
        tabuleiro6 = MicroTabuleiro()
        tabuleiro7 = MicroTabuleiro()
        tabuleiro8 = MicroTabuleiro()
        tabuleiro9 = MicroTabuleiro()
        self.tabuleiro = [  [tabuleiro1, tabuleiro2, tabuleiro3],
                            [tabuleiro4, tabuleiro5, tabuleiro6],
                            [tabuleiro7, tabuleiro8, tabuleiro9]    ]

    def exibeTabuleiro(self):
        '''
        Exibe o macro tabuleiro.
        '''
        print()
        for j in range(0, 7, 3):
            for k in range(3):
                print(" ", end='')
                self.exibeLinha(j,k)
        print()

    def exibeLinha(self,j,k):
        '''
        k é a linha dos micro tabuleiros a ser exibida. j é o primeiro micro tabuleiro a ser exibido.
        A função exibe uma parte do macro tabuleiro: a linha k dos micro tabuleiros j, j+1 e j+2 (considerando
        que o macro tabuleiro possui micro tabuleiros identificados de 0 a 8).
        '''
        linha = j // 3
        for coluna in range(3):
            print("  ", end='')
            if (self.tabuleiro[linha][coluna] != "X") and (self.tabuleiro[linha][coluna] != "O"):
                print(self.tabuleiro[linha][coluna].retornaElemento(k,0), " | ", self.tabuleiro[linha][coluna].retornaElemento(k,1), " | ",
                        self.tabuleiro[linha][coluna].retornaElemento(k,2), " ", end='', sep='')
            elif self.tabuleiro[linha][coluna] == "X":
                if (k == 0) or (k == 2):
                    print("X       X ", end='')
                else:
                    print("    X     ", end='')
            else:
                if (k == 0) or (k == 2):
                    print("O O O O O", " ", end='', sep='')
                else:
                    print("O       O", " ", end='', sep='')
            if coluna != 2:
                print(" |", end='')
            else:
                print()
        print(" ", end='')
        if (k != 2):
            for coluna in range(3):
                if (self.tabuleiro[linha][coluna] != "X") and (self.tabuleiro[linha][coluna] != "O"):
                    print(" -----------", end='')
                elif self.tabuleiro[linha][coluna] == "X":
                    print("    X   X   ", end='')
                else:
                    print("  O       O ", end='')
                if coluna != 2:
                    print(" |", end='')
                else:
                    print()
        elif j != 6:
            print("-----------------------------------------")
    
    def exibeMicro(self, indice):
        '''
        Recebe o índice (inteiro de 0 a 8) de um micro tabuleiro do macro tabuleiro.
        Exibe e retorna o micro tabuleiro correspondente ao índice dado.
        '''
        if indice < 3:
            linha = 0
            coluna = indice
        else:
            linha = indice // 3
            coluna = indice % (linha * 3)
        self.tabuleiro[linha][coluna].exibeTabuleiro()
        return(self.tabuleiro[linha][coluna])

class MicroTabuleiro(Tabuleiro):
    '''
    Abstração para um micro tabuleiro. É um Tabuleiro que pode ocupar uma casa de um macro tabuleiro.
    '''

    def __init__(self):
        Tabuleiro.__init__(self)
        self.tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def retornaElemento(self, linha, coluna):
        '''
        Dada uma linha e uma coluna, retorna o elemento do micro tabuleiro correspondente à posição.
        '''
        return(self.tabuleiro[linha][coluna])

    def retornaListaElementos(self):
        '''
        Função exclusiva para micro tabuleiro que guarda as casas ainda não fechadas de um macro tabuleiro.
        Retorna uma lista com essas casas abertas (ou seja, casas com micro tabuleiros ainda não ganhos).
        '''
        lista = []
        for linha in range(3):
            for coluna in range(3):
                if type(self.tabuleiro[linha][coluna]) == int:
                    lista.append(self.tabuleiro[linha][coluna])
        return(lista)
    
    def retornaLinhasAbertas(self):
        '''
        Verifica quais linhas do micro tabuleiro ainda podem receber jogadas.
        Retorna uma lista com essas linhas.
        Função usada para verificar se a linha de jogada dada pelo usuário é válida.
        '''
        linhas_abertas = []
        for linha in range(3):
            aberta = False
            for coluna in range(3):
                if (self.tabuleiro[linha][coluna] != "X") and (self.tabuleiro[linha][coluna] != "O"):
                    aberta = True
            if aberta:
                linhas_abertas.append(linha + 1)
        return(linhas_abertas)
    
    def retornaColunasAbertas(self, linha):
        '''
        Verifica quais colunas de uma linha dada do micro tabuleiro ainda podem receber jogadas.
        Retorna uma lista com essas colunas.
        Função usada para verificar se a coluna de jogada dada pelo usuário é válida.
        '''
        colunas_abertas = []
        for coluna in range(3):
            if (self.tabuleiro[linha][coluna] != "X") and (self.tabuleiro[linha][coluna] != "O"):
                colunas_abertas.append(coluna + 1)
        return(colunas_abertas)

    def exibeTabuleiro(self):
        '''
        Exibe um micro tabuleiro.
        '''
        print()
        for i in range(3):
            print(" ", end='')
            for j in range(3):
                print(" " + str(self.tabuleiro[i][j]) + " ", end='')
                if j != 2:
                    print("|", end='')
            print()
            if i != 2:
                print(" -----------")
        print()

class Jogador:
    '''
    Abstração para um jogador do jogo da velha ultimate. É uma "superclasse" dos diferentes tipos de jogadores.
    '''
    def __init__(self):
        self.simbolo = ""
    def mudaSimbolo(self, simbolo):
        self.simbolo = simbolo
    def retornaSimbolo(self):
        return(self.simbolo)

class JogadorHumano(Jogador):
    '''
    Abstração para o jogador controlado por um usuário, o qual escolhe tabuleiros, linhas e colunas
    a partir de chamadas no terminal.
    '''
    def __init__(self):
        Jogador.__init__(self)

    def escolheTabuleiro(self, lista_tabuleiros):
        '''
        Recebe do usuário um tabuleiro válido no qual deseja jogar.
        '''
        escolha = input()
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in lista_tabuleiros:
            print("Tabuleiro escolhido inválido. Tente novamente.")
            escolha = input("Tabuleiro escolhido: ")
            try:
                escolha = int(escolha)
            except:
                escolha = -1
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Recebe do usuário uma linha válida do tabuleiro escolhido na qual deseja jogar.
        '''
        escolha = input("Linha escolhida: ")
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in linhas_abertas:
            print("Linha escolhida inválida. Tente novamente.")
            escolha = input("Linha escolhida: ")
            try:
                escolha = int(escolha)
            except:
                escolha = -1
        return(escolha)
    
    def escolheColuna(self, colunas_abertas):
        '''
        Recebe do usuário uma coluna válida do tabuleiro e da linha escolhida na qual deseja jogar.
        '''
        escolha = input("Coluna escolhida: ")
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in colunas_abertas:
            print("Coluna escolhida inválida. Tente novamente.")
            escolha = input("Coluna escolhida: ")
            try:
                escolha = int(escolha)
            except:
                escolha = -1
        return(escolha)

class JogadorAleatorio(Jogador):
    '''
    Abstração para um jogador automático que escolhe tabuleiros, linhas e colunas de maneira aleatória.
    Para que sejam definidas suas escolhas, é utilizada a biblioteca Random.
    '''
    def __init__(self):
        Jogador.__init__(self)

    def escolheTabuleiro(self, lista_tabuleiros):
        '''
        Escolhe, de maneira aleatória, um tabuleiro válido no qual irá jogar.
        '''
        escolha = random.choice(lista_tabuleiros)
        print(escolha)
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Escolhe, de maneira aleatória, uma linha válida no tabuleiro escolhido para jogar.
        '''
        escolha = random.choice(linhas_abertas)
        print("Linha escolhida:", escolha)
        return(escolha)

    def escolheColuna(self, colunas_abertas):
        '''
        Escolhe, de maneira aleatória, uma coluna válida no tabuleiro e na linha escolhida para jogar.
        '''
        escolha = random.choice(colunas_abertas)
        print("Coluna escolhida:", escolha)
        return(escolha)

class JogadorComeCru(Jogador):
    '''
    Abstração para um jogador automático que joga sempre no primeiro tabuleiro e na primeira posição disponíveis.
    '''
    def __init__(self):
        Jogador.__init__(self)

    def escolheTabuleiro(self, lista_tabuleiros):
        '''
        Escolhe o primeiro tabuleiro válido para jogar.
        '''
        escolha = lista_tabuleiros[0]
        print(escolha)
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Escolhe a primeira linha válida no tabuleiro escolhido para jogar.
        '''
        escolha = linhas_abertas[0]
        print("Linha escolhida:", escolha)
        return(escolha)

    def escolheColuna(self, colunas_abertas):
        '''
        Escolhe a primeira coluna válida no tabuleiro e na linha escolhida para jogar.
        '''
        escolha = colunas_abertas[0]
        print("Coluna escolhida:", escolha)
        return(escolha)

class JogoDaVelha_Ultimate:
    '''
    Abstração para o Jogo da Velha Ultimate.
    Ele é composto por um macro tabuleiro que contém, em cada uma de suas 9 casas, um micro tabuleiro.
    '''
    def __init__(self):
        self.macro_tabuleiro = MacroTabuleiro()
        self.num_rodadas = 0

    def iniciar(self):
        '''
        Inicia o jogo, exibindo um menu de início (para definir os tipos de jogadores), executando o laço
        do jogo e, por fim, finalizando a execução do programa.
        '''
        self.exibeMenu()
        self.laçoJogo()
        exit()
    
    def criaListaTabuleiros(self):
        '''
        Chamado no início da execução do jogo, cria um micro tabuleiro que guarda as casas do macro tabuleiro
        que ainda podem receber jogadas (ou seja, guarda os micro tabuleiros ainda abertos).
        '''
        self.lista_tabuleiros = MicroTabuleiro()
        for linha in range (3):
            for coluna in range (3):
                self.lista_tabuleiros.alteraTabuleiro(linha, coluna, (coluna + 3*linha + 1))

    def exibeMenu(self):
        '''
        Exibe um menu de inicialização que define algumas condições para a execução do jogo.
        Chamada métodos para definição dos tipos dos jogadores e também a ordem em que jogarão.
        '''
        input("Bem-Vindo ao Ultimate TicTacToe\n(Pressione Enter) ")
        self.criaListaTabuleiros()
        self.criaJogadores()
        self.jogador1.mudaSimbolo("O")
        print("\nO Jogador 1 jogará com 'O'")
        self.jogador2.mudaSimbolo("X")
        print("O Jogador 2 jogará com 'X'")
        self.jogador_atual = random.randint(0,1) # define o jogador que inicia
        print("\nO Jogador", self.jogador_atual + 1, "foi sorteado para começar!\n")

    def criaJogadores(self):
        '''
        Permite a definição dos tipos dos jogadores e sua criação, de acordo com respostas do(s) usuário(s).
        '''
        tipo_jogador1 = -1
        tipo_jogador2 = -1
        primeira_tentativa = True
        while (tipo_jogador1 != 0) and (tipo_jogador1 != 1) and (tipo_jogador1 != 2):
            if primeira_tentativa:
                primeira_tentativa = False
            else:
                print("Tipo de Jogador inválido. Tente Novamente.")
            tipo_jogador1 = input("\nEscolha o tipo do Jogador 1:\n(0) Humano\n(1) Aleatorio\n(2) Come-cru\n\nSua escolha: ")
            try:
                tipo_jogador1 = int(tipo_jogador1)
            except:
                tipo_jogador1 = -1
        primeira_tentativa = True
        while (tipo_jogador2 != 0) and (tipo_jogador2 != 1) and (tipo_jogador2 != 2):
            if primeira_tentativa:
                primeira_tentativa = False
            else:
                print("Tipo de Jogador inválido. Tente Novamente.")
            tipo_jogador2 = input("\nEscolha o tipo do Jogador 2:\n(0) Humano\n(1) Aleatorio\n(2) Come-cru\n\nSua escolha: ")
            try:
                tipo_jogador2 = int(tipo_jogador2)
            except:
                tipo_jogador2 = -1
        if tipo_jogador1 == 0:
            self.jogador1 = JogadorHumano()
        elif tipo_jogador1 == 1:
            self.jogador1 = JogadorAleatorio()
        else:
            self.jogador1 = JogadorComeCru()
        if tipo_jogador2 == 0:
            self.jogador2 = JogadorHumano()
        elif tipo_jogador2 == 1:
            self.jogador2 = JogadorAleatorio()
        else:
            self.jogador2 = JogadorComeCru()
        self.jogadores = [self.jogador1, self.jogador2]
    
    def atualizaMacro(self, micro_tabuleiro, indice):
        '''
        Após uma alteração em um dos micro tabuleiros, verifica se ele foi fechado.
        -   Em caso positivo, e com um vencedor, atualiza o macro tabuleiro para que defina a casa fechada
            como pertencente ao jogador que a venceu, e a torna inacessível para receber jogadas.
        -   Caso fechado, mas tendo dado velha, é feito um sorteio para definir a quem pertencerá a casa
            fechada ("cara ou coroa").
        '''
        acabou = micro_tabuleiro.chegouAoFim()
        if not acabou: # ainda não tem vencedor no micro tabuleiro dado
            return
        else:
            if indice < 3:
                linha = 0
                coluna = indice
            else:
                linha = indice // 3
                coluna = indice % (linha * 3)
            if acabou == -1: # deu velha
                print("Deu velha no tabuleiro", indice + 1)
                print("Então, vamos jogador uma moeda para decidir seu vencedor!")
                print("Se der cara, o Jogador 1 venceu. Se der coroa, o Jogador 2 é que está com sorte.")
                print("Jogando a moeda...\n")
                moeda = random.randint(1,2)
                if moeda == 1:
                    print("DEU CARA: o Jogador 1 venceu o tabuleiro ", indice + 1, "!", sep='')
                    simbolo = self.jogador1.retornaSimbolo()
                elif moeda == 2:
                    print("DEU COROA: o Jogador 2 venceu o tabuleiro ", indice + 1, "!", sep='')
                    simbolo = self.jogador2.retornaSimbolo()
            elif acabou == 1: # Jogador 1 venceu
                print("O Jogador 1 venceu o tabuleiro ", indice + 1, "!", sep='')
                simbolo = self.jogador1.retornaSimbolo()
            elif acabou == 2: # Jogador 2 venceu
                print("O Jogador 2 venceu o tabuleiro ", indice + 1, "!", sep='')
                simbolo = self.jogador2.retornaSimbolo()
            self.lista_tabuleiros.alteraTabuleiro(linha, coluna, simbolo)
            self.macro_tabuleiro.alteraTabuleiro(linha, coluna, simbolo)

    def laçoJogo(self):
        '''
        Executa o laço do jogo, que se repete até o macro tabuleiro ser fechado.
        Ao final, verifica se o jogo teve um vencedor ou se deu velha.
        '''
        primeira_rodada = True
        while not self.macro_tabuleiro.chegouAoFim():
            if primeira_rodada:
                primeira_rodada = False
            else:
                self.jogador_atual = (self.jogador_atual + 1) % 2 # alternar entre jogador 1 e 2
            self.geraRodada()
        vencedor = self.macro_tabuleiro.chegouAoFim()
        self.macro_tabuleiro.exibeTabuleiro()
        if vencedor == -1:
            print("DEU VELHA NO MACRO TABULEIRO!")
            print("OCORREU UM EMPATE! PARABÉNS AOS DOIS JOGADORES!")
            return
        else:
            print("O JOGADOR", vencedor, "VENCEU O ULTIMATE TIC-TAC-TOE!")
            print("PARABÉNS AOS PARTICIPANTES!")
            return

    def geraRodada(self):
        '''
        Gera uma rodada do jogo, recebendo as ações dos dois jogadores.
        '''
        input("(Pressione Enter para continuar) ")
        self.num_rodadas += 1
        print("\n====================== RODADA", self.num_rodadas, "======================\n")
        # executa a rodada para o primeiro jogador
        self.geraSubRodada()
        self.macro_tabuleiro.exibeTabuleiro()
        input("Pressione Enter para continuar ")
        if not self.macro_tabuleiro.chegouAoFim():
            # alternar entre jogador 1 e 2
            self.jogador_atual = (self.jogador_atual + 1) % 2
            # executa a rodada para o segundo jogador
            print()
            self.geraSubRodada()
            self.macro_tabuleiro.exibeTabuleiro()

    def geraSubRodada(self):
        '''
        Gera uma subrodada, correspondendo à ação de um jogador (recebe a ação de um único jogador).
        '''
        print("Vez do Jogador ", self.jogador_atual + 1, "!", sep='')
        self.macro_tabuleiro.exibeTabuleiro()
        self.recebeJogada(self.jogadores[self.jogador_atual])

    def recebeJogada(self, jogador):
        '''
        Recebe do usuário tabuleiro, linha e coluna válidos e executa a jogada.
        '''
        # --- recebe o tabuleiro que receberá a jogada ---
        print("Em qual tabuleiro você deseja jogar?")
        self.lista_tabuleiros.exibeTabuleiro()
        print("Tabuleiro escolhido: ", end='')
        numero_tabuleiro = (jogador.escolheTabuleiro(self.lista_tabuleiros.retornaListaElementos())) - 1
        tabuleiro_escolhido = self.macro_tabuleiro.exibeMicro(numero_tabuleiro)
        # --- recebe a linha que receberá a jogada ---
        print("Em qual linha você deseja jogar?")
        print("Linhas disponíveis:", end='')
        linhas_abertas = tabuleiro_escolhido.retornaLinhasAbertas()
        for linha in linhas_abertas:
            print(" ", linha, sep='', end='')
        print()
        linha_escolhida = (jogador.escolheLinha(linhas_abertas)) - 1
        # --- recebe a coluna que receberá a jogada ---
        print("\nEm qual coluna você deseja jogar?")
        print("Colunas disponíveis:", end='')
        colunas_abertas = tabuleiro_escolhido.retornaColunasAbertas(linha_escolhida)
        for coluna in colunas_abertas:
            print(" ", coluna, sep='', end='')
        print()
        coluna_escolhida = (jogador.escolheColuna(colunas_abertas)) - 1
        # --- faz a jogada na posição escolhida ---
        simbolo_jogador = jogador.retornaSimbolo()
        tabuleiro_escolhido.alteraTabuleiro(linha_escolhida, coluna_escolhida, simbolo_jogador)
        tabuleiro_escolhido.exibeTabuleiro()
        self.atualizaMacro(tabuleiro_escolhido, numero_tabuleiro)

def main():
    jogo = JogoDaVelha_Ultimate()
    jogo.iniciar()

if __name__ == "__main__":
    main()