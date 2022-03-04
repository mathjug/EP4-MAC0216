'''
EP4 MAC0216
INTEGRANTES: Matheus Sanches Jurgensen (12542199), Caio Rodrigues Gama (12543381)
DATA: 10/12/2021

EXTRAS IMPLEMENTADOS: Inteligência Artificial e "Random turn tic-tac-toe".
'''

import random

class Tabuleiro:
    '''
    Abstração para um tabuleiro de jogo da velha.
    '''
    def __init__(self):
        self.tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def alteraTabuleiro(self, linha, coluna, elemento):
        '''
        Recebendo uma linha, uma coluna e um elemento, atribui esse elemento à posição do tabuleiro
        dada pela linha e pela coluna.
        '''
        self.tabuleiro[linha][coluna] = elemento
    
    def retornaElemento(self, linha, coluna):
        '''
        Dada uma linha e uma coluna, retorna o elemento do tabuleiro correspondente à posição.
        '''
        return(self.tabuleiro[linha][coluna])
    
    def retornaLinhasAbertas(self):
        '''
        
        Verifica quais linhas do tabuleiro ainda podem receber jogadas.
        Retorna uma lista com essas linhas.
        '''
        linhas_abertas = []
        for linha in range(3):
            aberta = False
            for coluna in range(3):
                if self.tabuleiro[linha][coluna] not in ["X", "O"]:
                    aberta = True
            if aberta:
                linhas_abertas.append(linha + 1)
        return(linhas_abertas)
    
    def retornaColunasAbertas(self, linha):
        '''
        Verifica quais colunas de uma linha dada do tabuleiro ainda podem receber jogadas.
        Retorna uma lista com essas colunas.
        '''
        colunas_abertas = []
        for coluna in range(3):
            if self.tabuleiro[linha][coluna] not in ["X", "O"]:
                colunas_abertas.append(coluna + 1)
        return(colunas_abertas)

    def exibeTabuleiro(self):
        '''
        Exibe um tabuleiro de jogo da velha.
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
    Abstração para um macro tabuleiro do Jogo da Velha Ultimate. É um Tabuleiro cujas casas são compostas
    por outros tabuleiros. Esses outros tabuleiros são referidos em alguns métodos como micro tabuleiros,
    apenas para facilitar a distinção, apesar de serem simples tabuleiros da classe Tabuleiro. Em geral, o
    usuário se refere às casas do macro tabuleiro de 1 a 9, da seguinte forma:
     1 | 2 | 3 
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    No entanto, para facilitar a implementação, alguns métodos se referem às casas do macro tabuleiro de 0 a 8:
     0 | 1 | 2 
    -----------
     3 | 4 | 5
    -----------
     6 | 7 | 8
    '''
    def __init__(self):
        Tabuleiro.__init__(self)
        for linha in range(3):
            for coluna in range(3):
                self.tabuleiro[linha][coluna] = Tabuleiro()

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
        k é a linha dos (micro) tabuleiros a ser exibida. j é o primeiro (micro) tabuleiro a ser exibido.
        A função exibe uma parte do macro tabuleiro: a linha k dos tabuleiros j, j+1 e j+2 (considerando que
        o macro tabuleiro possui tabuleiros identificados de 0 a 8). É uma função auxiliar do método
        exibeTabuleiro() desta classe MacroTabuleiro.
        '''
        linha = j // 3
        for coluna in range(3):
            print("  ", end='')
            if self.tabuleiro[linha][coluna] not in ["X", "O"]:
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
                if self.tabuleiro[linha][coluna] not in ["X", "O"]:
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
        Recebe o índice (inteiro de 0 a 8) de um (micro) tabuleiro do macro tabuleiro.
        Exibe e retorna o (micro) tabuleiro correspondente ao índice dado.
        '''
        if indice < 3:
            linha = 0
            coluna = indice
        else:
            linha = indice // 3
            coluna = indice % (linha * 3)
        self.tabuleiro[linha][coluna].exibeTabuleiro()
        return(self.tabuleiro[linha][coluna])

class TabuleiroDeNumeros(Tabuleiro):
    '''
    Abstração para um tabuleiro que guarda os índices dos (micro) tabuleiros que compõem um macro.
    Para um (micro) tabuleiro ainda não completo, o tabuleiro de números guarda, na posição correspondente,
    o seu índice (inteiro de 1 a 9). No entanto, se ele já estiver completo, o tabuleiro de números guarda,
    em sua posição, "X" ou "O", dependendo de quem o tiver vencido.
    Exemplo de seu atributo "tabuleiro": [[1, 2, "X"], ["O", 5, "X"], [7, 8, 9]]
    '''
    def __init__(self):
        Tabuleiro.__init__(self)
        for linha in range (3):
            for coluna in range (3):
                self.tabuleiro[linha][coluna] = coluna + 3*linha + 1
    
    def retornaListaAbertos(self):
        '''
        Retorna uma lista com as casas abertas de um macro tabuleiro, a partir das informações do tabuleiro
        de números (ou seja, retorna lista com os números dos (micro) tabuleiros ainda não ganhos).
        '''
        lista = []
        for linha in range(3):
            for coluna in range(3):
                if type(self.tabuleiro[linha][coluna]) == int:
                    lista.append(self.tabuleiro[linha][coluna])
        return(lista)

class Jogador:
    '''
    Abstração para um jogador do Jogo da Velha Ultimate. É uma "superclasse" dos diferentes tipos de jogadores.
    '''
    def __init__(self):
        self.simbolo = ""

    def mudaSimbolo(self, simbolo):
        '''
        Atribui ao atributo "simbolo" da classe aquele que é passado como argumento.
        '''
        self.simbolo = simbolo

    def retornaSimbolo(self):
        '''
        Retorna o símbolo do jogador.
        '''
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
        Retorna o tabuleiro válido no qual o usuário humano deseja jogar.
        Portanto, faz chamadas ao usuário até que ele escolha um tabuleiro válido.
        '''
        escolha = input("Tabuleiro escolhido: ")
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in lista_tabuleiros:
            print("[ULTIMATE TIC-TAC-TOE] Tabuleiro escolhido inválido. Tente novamente.")
            escolha = input("Tabuleiro escolhido: ")
            try:
                escolha = int(escolha)
            except:
                escolha = -1
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Retorna a linha válida do tabuleiro escolhido na qual o usuário humano deseja jogar.
        Portanto, faz chamadas ao usuário até que ele escolha uma linha válida.
        '''
        escolha = input("Linha escolhida: ")
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in linhas_abertas:
            print("[ULTIMATE TIC-TAC-TOE] Linha escolhida inválida. Tente novamente.")
            escolha = input("Linha escolhida: ")
            try:
                escolha = int(escolha)
            except:
                escolha = -1
        return(escolha)
    
    def escolheColuna(self, colunas_abertas):
        '''
        Retorna a coluna válida da linha do tabuleiro escolhido na qual o usuário humano deseja jogar.
        Portanto, faz chamadas ao usuário até que ele escolha uma coluna válida.
        '''
        escolha = input("Coluna escolhida: ")
        try:
            escolha = int(escolha)
        except:
            escolha = -1
        while escolha not in colunas_abertas:
            print("[ULTIMATE TIC-TAC-TOE] Coluna escolhida inválida. Tente novamente.")
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
        Escolhe e retorna, de maneira aleatória, um tabuleiro válido no qual o jogador aleatório irá jogar.
        '''
        escolha = random.choice(lista_tabuleiros)
        print("Tabuleiro escolhido:", escolha)
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Escolhe e retorna, de maneira aleatória, uma linha válida no tabuleiro escolhido para jogar.
        '''
        escolha = random.choice(linhas_abertas)
        print("Linha escolhida:", escolha)
        return(escolha)

    def escolheColuna(self, colunas_abertas):
        '''
        Escolhe e retorna, de maneira aleatória, uma coluna válida no tabuleiro e na linha escolhidos para jogar.
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
        Escolhe e retorna o primeiro tabuleiro válido no qual o jogador come-cru irá jogar.
        '''
        escolha = lista_tabuleiros[0]
        print("Tabuleiro escolhido:", escolha)
        return(escolha)

    def escolheLinha(self, linhas_abertas):
        '''
        Escolhe e retorna a primeira linha válida no tabuleiro escolhido para jogar.
        '''
        escolha = linhas_abertas[0]
        print("Linha escolhida:", escolha)
        return(escolha)

    def escolheColuna(self, colunas_abertas):
        '''
        Escolhe e retorna a primeira coluna válida no tabuleiro e na linha escolhidos para jogar.
        '''
        escolha = colunas_abertas[0]
        print("Coluna escolhida:", escolha)
        return(escolha)

class JogadorInteligente(Jogador):
    '''
    Abstração para um jogador automático que faz suas jogadas de maneira inteligente, seguindo alguns padrões:
    - ESCOLHA DO TABULEIRO: Se for a primeira jogada da partida, joga no primeiro tabuleiro.
                            Caso contrário, joga no último tabuleiro que recebeu jogada. No entanto, se esse
                            tabuleiro tiver sido fechado, joga em um aleatório disponível.
    - ESCOLHA DA CASA:      Busca uma posição não ocupada e que pode levar a uma solução. Caso não houver
                            possível solução, joga na primeira casa disponível.
    '''
    def __init__(self):
        Jogador.__init__(self)
    
    def escolheTabuleiro(self, lista_tabuleiros, ultimo_tabuleiro):
        '''
        Escolhe e retorna o tabuleiro em que fará a jogada, segundo o método de decisão definido na classe.
        '''
        if ultimo_tabuleiro == -1:
            escolha = 1
        elif ultimo_tabuleiro not in lista_tabuleiros:
            escolha = random.choice(lista_tabuleiros)
        else:
            escolha = ultimo_tabuleiro
        print("Tabuleiro escolhido:", escolha)
        return(escolha)

    def escolheLinha(self, tabuleiro):
        '''
        Escolhe e retorna a linha válida em que fará a jogada, segundo o método de decisão definido na classe.
        Devido à maneira como foi implementado o método, ele encontra, também, a coluna em que será feita a jogada.
        Essa coluna é salva como atributo.
        '''
        # verifica se há uma linha inteira apenas com espaços e o símbolo do jogador
        for linha in range(3):
            for coluna in range(3):
                elemento = tabuleiro.retornaElemento(linha, coluna)
                if elemento == " ":
                    self.coluna_escolhida = coluna + 1
                elif elemento != self.simbolo:
                    break
                if coluna == 2:
                    escolha = linha + 1
                    print("Linha escolhida:", escolha)
                    return(escolha)

        # verifica se há uma coluna inteira apenas com espaços e o símbolo do jogador
        for coluna in range(3):
            for linha in range(3):
                elemento = tabuleiro.retornaElemento(linha, coluna)
                if elemento == " ":
                    escolha = linha + 1
                elif elemento != self.simbolo:
                    break
                if linha == 2:
                    self.coluna_escolhida = coluna + 1
                    print("Linha escolhida:", escolha)
                    return(escolha)
        
        # verifica se há uma diagonal inteira apenas com espaços e o símbolo do jogador
        # 1) verifica diagonal principal
        for linha in range(3):
            elemento = tabuleiro.retornaElemento(linha, linha)
            if elemento == " ":
                self.coluna_escolhida = linha + 1
                escolha = linha + 1
            elif elemento != self.simbolo:
                break
            if linha == 2:
                print("Linha escolhida:", escolha)
                return(escolha)
        # 2) verifica diagonal secundária
        for linha in range(3):
            coluna = 2 - linha
            elemento = tabuleiro.retornaElemento(linha, coluna)
            if elemento == " ":
                self.coluna_escolhida = coluna + 1
                escolha = linha + 1
            elif elemento != self.simbolo:
                break
            if linha == 2:
                print("Linha escolhida:", escolha)
                return(escolha)
        
        # como não achou uma posição promissora, joga na primeira casa disponível
        escolha = tabuleiro.retornaLinhasAbertas()[0]
        self.coluna_escolhida = tabuleiro.retornaColunasAbertas(escolha - 1)[0]
        print("Linha escolhida:", escolha)
        return(escolha)

    def escolheColuna(self, colunas_abertas):
        '''
        Retorna a coluna válida em que fará a jogada.
        '''
        return(self.coluna_escolhida)

class AlternadorDeJogadores:
    '''
    Abstração para um mecanismo que define qual jogador deve fazer sua jogada na rodada corrente.
    O objeto deve ser criado especificando-se o seu modo de atuação, segundo as duas opções abaixo:
    - MODO 1: jogadores alternados (um jogador nunca faz duas jogadas seguidas)
    - MODO 2: jogadores aleatórios (usa a biblioteca Random para definir quem faz cada jogada)
    '''
    def __init__(self, modo):
        self.modo = modo

    def defineQuemComeca(self):
        '''
        Executado no começo do jogo, esse método define qual jogador faz a primeira jogada.
        '''
        return(random.randint(0,1))

    def alternaJogador(self, jogador_atual):
        '''
        De acordo com o modo de alternância de jogadores especificado, define quem deve fazer a jogada.
        '''
        if self.modo == 1:
            return((jogador_atual + 1) % 2)
        elif self.modo == 2:
            return(random.randint(0,1))
    
class JogoDaVelha_Ultimate:
    '''
    Abstração para o Jogo da Velha Ultimate.
    Ele é composto por um macro tabuleiro que contém, em cada uma de suas 9 casas, um novo tabuleiro.
    '''
    def __init__(self):
        self.macro_tabuleiro = MacroTabuleiro()
        self.lista_tabuleiros = TabuleiroDeNumeros()
        self.ultimo_tabuleiro_jogado = -1
        self.num_rodadas = 0

    def iniciar(self):
        '''
        Inicia o jogo, exibindo um menu de início (para definir os tipos de jogadores), executando o laço
        do jogo e, por fim, finalizando a execução do programa.
        '''
        self.exibeMenu()
        self.laçoJogo()
        return

    def exibeMenu(self):
        '''
        Exibe um menu de inicialização que define algumas condições para a execução do jogo.
        Chama métodos para a definição dos tipos dos jogadores e também a ordem em que jogarão.
        '''
        input("=============== Bem-Vindo ao Ultimate TicTacToe ===============\n(Pressione Enter) ")
        self.criaJogadores()
        self.jogadores[0].mudaSimbolo("O")
        print("\nO Jogador 1 jogará com 'O'")
        self.jogadores[1].mudaSimbolo("X")
        print("O Jogador 2 jogará com 'X'")
        input("\n(Pressione Enter para continuar) ")
        print("\n+ Escolha o modo de alternância dos jogadores:")
        print("[1] Alternado simples (um jogador não faz duas jogadas seguidas)")
        print("[2] Aleatório (a cada rodada, define-se quem joga de maneira aleatória)")
        modo_alternancia = input("\nSua escolha: ") # define como os jogadores são alternados a cada rodada
        while modo_alternancia not in ["1", "2"]:
            print("Modo inválido. Tente novamente.")
            modo_alternancia = input("\nSua escolha: ")
        self.alterna_jogadores = AlternadorDeJogadores(int(modo_alternancia))
        self.jogador_atual = self.alterna_jogadores.defineQuemComeca() # define o jogador que inicia
        print("\nO Jogador", self.jogador_atual + 1, "foi sorteado para começar!\n")

    def criaJogadores(self):
        '''
        Permite a definição dos tipos dos jogadores e sua criação, de acordo com respostas do(s) usuário(s).
        '''
        tipo_jogador1 = -1
        primeira_tentativa = True
        while tipo_jogador1 not in [0, 1, 2, 3]:
            if primeira_tentativa:
                primeira_tentativa = False
            else:
                print("[ULTIMATE TIC-TAC-TOE] Tipo de Jogador inválido. Tente Novamente.")
            tipo_jogador1 = input("\n+ Escolha o tipo do Jogador 1:\n[0] Humano\n[1] Aleatorio\n[2] Come-cru\n[3] Inteligente\n\nSua escolha: ")
            try:
                tipo_jogador1 = int(tipo_jogador1)
            except:
                tipo_jogador1 = -1
        tipo_jogador2 = -1
        primeira_tentativa = True
        while tipo_jogador2 not in [0, 1, 2, 3]:
            if primeira_tentativa:
                primeira_tentativa = False
            else:
                print("[ULTIMATE TIC-TAC-TOE] Tipo de Jogador inválido. Tente Novamente.")
            tipo_jogador2 = input("\n+ Escolha o tipo do Jogador 2:\n[0] Humano\n[1] Aleatorio\n[2] Come-cru\n[3] Inteligente\n\nSua escolha: ")
            try:
                tipo_jogador2 = int(tipo_jogador2)
            except:
                tipo_jogador2 = -1
        if tipo_jogador1 == 0:
            jogador1 = JogadorHumano()
        elif tipo_jogador1 == 1:
            jogador1 = JogadorAleatorio()
        elif tipo_jogador1 == 2:
            jogador1 = JogadorComeCru()
        elif tipo_jogador1 == 3:
            jogador1 = JogadorInteligente()
        if tipo_jogador2 == 0:
            jogador2 = JogadorHumano()
        elif tipo_jogador2 == 1:
            jogador2 = JogadorAleatorio()
        elif tipo_jogador2 == 2:
            jogador2 = JogadorComeCru()
        elif tipo_jogador2 == 3:
            jogador2 = JogadorInteligente()
        self.jogadores = [jogador1, jogador2]
        self.tipos_jogadores = [tipo_jogador1, tipo_jogador2]
    
    def atualizaMacro(self, tabuleiro, indice):
        '''
        Após uma alteração em um dos tabuleiros, verifica se ele foi fechado.
        -   Em caso positivo, e com um vencedor, atualiza o macro tabuleiro para que defina a casa fechada
            como pertencente ao jogador que a venceu, e a torna inacessível para receber jogadas.
        -   Caso fechado, mas tendo dado velha, é feito um sorteio para definir a quem pertencerá a casa
            fechada ("cara ou coroa").
        '''
        acabou = tabuleiro.chegouAoFim()
        if not acabou: # ainda não tem vencedor no tabuleiro dado
            return
        else:
            if indice < 3:
                linha = 0
                coluna = indice
            else:
                linha = indice // 3
                coluna = indice % (linha * 3)
            if acabou == -1: # deu velha
                print("[ULTIMATE TIC-TAC-TOE] Deu velha no tabuleiro", indice + 1)
                print("Então, vamos jogador uma moeda para decidir seu vencedor!")
                print("Se der cara, o Jogador 1 venceu. Se der coroa, o Jogador 2 é que está com sorte.")
                print("Jogando a moeda...\n")
                moeda = random.randint(1,2)
                if moeda == 1:
                    print("DEU CARA: o Jogador 1 venceu o tabuleiro ", indice + 1, "!", sep='')
                    simbolo = self.jogadores[0].retornaSimbolo()
                elif moeda == 2:
                    print("DEU COROA: o Jogador 2 venceu o tabuleiro ", indice + 1, "!", sep='')
                    simbolo = self.jogadores[1].retornaSimbolo()
            elif acabou == 1: # Jogador 1 venceu
                print("[ULTIMATE TIC-TAC-TOE] O Jogador 1 venceu o tabuleiro ", indice + 1, "!", sep='')
                simbolo = self.jogadores[0].retornaSimbolo()
            elif acabou == 2: # Jogador 2 venceu
                print("[ULTIMATE TIC-TAC-TOE] O Jogador 2 venceu o tabuleiro ", indice + 1, "!", sep='')
                simbolo = self.jogadores[1].retornaSimbolo()
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
                input("(Pressione Enter para continuar) ")
            else:
                self.jogador_atual = self.alterna_jogadores.alternaJogador(self.jogador_atual) # define quem joga
            self.geraRodada()
        vencedor = self.macro_tabuleiro.chegouAoFim()
        self.macro_tabuleiro.exibeTabuleiro()
        if vencedor == -1:
            print("[ULTIMATE TIC-TAC-TOE] DEU VELHA NO MACRO TABULEIRO!")
            print("OCORREU UM EMPATE! PARABÉNS AOS PARTICIPANTES!")
            return
        else:
            print("[ULTIMATE TIC-TAC-TOE] O JOGADOR", vencedor, "VENCEU O ULTIMATE TIC-TAC-TOE!")
            print("PARABÉNS AOS PARTICIPANTES!")
            return

    def geraRodada(self):
        '''
        Gera uma rodada do jogo, recebendo as ações dos dois jogadores (2 subrodadas).
        '''
        self.num_rodadas += 1
        print("\n========================= RODADA", self.num_rodadas, "=========================\n")
        # executa a rodada para o primeiro jogador
        self.geraSubRodada()
        self.macro_tabuleiro.exibeTabuleiro()
        input("(Pressione Enter para continuar) ")
        if not self.macro_tabuleiro.chegouAoFim():
            # define quem joga
            print("\nDefinindo quem deve fazer a jogada...")
            self.jogador_atual = self.alterna_jogadores.alternaJogador(self.jogador_atual)
            # executa a rodada para o segundo jogador
            self.geraSubRodada()
            self.macro_tabuleiro.exibeTabuleiro()
            input("(Pressione Enter para continuar) ")

    def geraSubRodada(self):
        '''
        Gera uma subrodada, correspondendo à ação de um jogador (recebe a ação de um único jogador).
        '''
        print("Vez do Jogador ", self.jogador_atual + 1, "!", sep='')
        self.macro_tabuleiro.exibeTabuleiro()
        self.recebeJogada(self.jogadores[self.jogador_atual], self.tipos_jogadores[self.jogador_atual])

    def recebeJogada(self, jogador, tipo_jogador):
        '''
        Solicita ao usuário tabuleiro, linha e coluna válidos e executa a jogada.
        '''
        # --- recebe o tabuleiro que receberá a jogada ---
        print("[ULTIMATE TIC-TAC-TOE] Em qual tabuleiro você deseja jogar?")
        self.lista_tabuleiros.exibeTabuleiro()
        if tipo_jogador == 3:
            numero_tabuleiro = (jogador.escolheTabuleiro(self.lista_tabuleiros.retornaListaAbertos(), self.ultimo_tabuleiro_jogado)) - 1
        else:
            numero_tabuleiro = (jogador.escolheTabuleiro(self.lista_tabuleiros.retornaListaAbertos())) - 1
        self.ultimo_tabuleiro_jogado = numero_tabuleiro + 1
        tabuleiro_escolhido = self.macro_tabuleiro.exibeMicro(numero_tabuleiro)
        # --- recebe a linha que receberá a jogada ---
        print("[ULTIMATE TIC-TAC-TOE] Em qual linha você deseja jogar?")
        print("[ULTIMATE TIC-TAC-TOE] Linhas disponíveis:", end='')
        linhas_abertas = tabuleiro_escolhido.retornaLinhasAbertas()
        for linha in linhas_abertas:
            print(" ", linha, sep='', end='')
        print()
        if tipo_jogador == 3:
            linha_escolhida = (jogador.escolheLinha(tabuleiro_escolhido)) - 1
        else:
            linha_escolhida = (jogador.escolheLinha(linhas_abertas)) - 1
        # --- recebe a coluna que receberá a jogada ---
        print("\n[ULTIMATE TIC-TAC-TOE] Em qual coluna você deseja jogar?")
        print("[ULTIMATE TIC-TAC-TOE] Colunas disponíveis:", end='')
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