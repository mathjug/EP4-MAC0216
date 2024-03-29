import pytest
from JogodaVelha import *

@pytest.fixture
def tabuleiro_exemplo():
    exemplo = Tabuleiro()
    exemplo.alteraTabuleiro(0,1,"X")
    return exemplo

@pytest.fixture
def tabuleiro_preenchido():
    preenchido = Tabuleiro()
    for linha in range(0, 3, 2):
        for coluna in range(3):
            preenchido.alteraTabuleiro(linha, coluna, "O")
    preenchido.alteraTabuleiro(1, 0, "X")
    preenchido.alteraTabuleiro(1, 2, "X")
    return preenchido

@pytest.fixture
def tabuleiro_velha():
    velha = Tabuleiro()
    velha.defineTabuleiro([["X", "O", "O"], ["O", "O", "X"], ["X", "X", "O"]])
    return velha

class TestaTabuleiro:
    # TESTA O CONSTRUTOR
    def test_init(self):
        tabuleiro_teste = Tabuleiro()
        assert tabuleiro_teste.tabuleiro == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] and type(tabuleiro_teste) == Tabuleiro

    # TESTAM MÉTODO QUE ALTERA O TABULEIRO
    def test_alteraTabuleiro_valido(self, tabuleiro_exemplo):
        saida_erro = tabuleiro_exemplo.alteraTabuleiro(2, 2, "O")
        assert tabuleiro_exemplo.tabuleiro[2][2] == "O"
        assert saida_erro == None
    def test_alteraTabuleiro_invalido(self, tabuleiro_exemplo):
        saida_erro = tabuleiro_exemplo.alteraTabuleiro(-1, 20, "O")
        assert saida_erro == -1
    
    # TESTAM MÉTODO QUE RETORNA ELEMENTO DO TABULEIRO
    def test_retornaElemento_valido(self, tabuleiro_exemplo):
        elemento = tabuleiro_exemplo.retornaElemento(0,1)
        assert elemento == "X"
    def test_retornaElemento_invalido(self, tabuleiro_exemplo):
        elemento = tabuleiro_exemplo.retornaElemento(500, 1)
        assert elemento == -1
    
    # TESTA MÉTODO QUE RETORNA LINHAS QUE AINDA NÃO FORAM COMPLETAS
    def test_retornaLinhasAbertas(self, tabuleiro_preenchido):
        lista = tabuleiro_preenchido.retornaLinhasAbertas()
        assert lista == [2]

    # TESTAM MÉTODO QUE RETORNA COLUNAS DE UMA LINHA QUE AINDA NÃO FORAM COMPLETAS
    def test_retornaColunasAbertas(self, tabuleiro_preenchido):
        lista = tabuleiro_preenchido.retornaColunasAbertas(1)
        assert lista == [2]
    def test_retornaColunasAbertas_vazio(self, tabuleiro_preenchido):
        lista = tabuleiro_preenchido.retornaColunasAbertas(0)
        assert lista == []
    
    # TESTAM MÉTODO QUE VERIFICA SE TABULEIRO JÁ FOI FECHADO
    def test_chegouAoFim_aberto(self, tabuleiro_exemplo):
        acabou = tabuleiro_exemplo.chegouAoFim()
        assert acabou == 0
    def test_chegouAoFim_jogador1_linha(self, tabuleiro_preenchido):
        acabou = tabuleiro_preenchido.chegouAoFim()
        assert acabou == 1
    def test_chegouAoFim_jogador1_diagonal(self):
        tabuleiro_teste = Tabuleiro()
        for linha in range(3):
            tabuleiro_teste.alteraTabuleiro(linha, linha, "O")
        acabou = tabuleiro_teste.chegouAoFim()
        assert acabou == 1
    def test_chegouAoFim_jogador2_coluna(self):
        tabuleiro_teste = Tabuleiro()
        for linha in range(3):
            tabuleiro_teste.alteraTabuleiro(linha, 0, "X")
        acabou = tabuleiro_teste.chegouAoFim()
        assert acabou == 2
    def test_chegouAoFim_velha(self, tabuleiro_velha):
        acabou = tabuleiro_velha.chegouAoFim()
        assert acabou == -1


@pytest.fixture
def macrotabuleiro_exemplo():
    exemplo = MacroTabuleiro()
    return exemplo

@pytest.fixture
def macrotabuleiro_linha_fechada():
    macro = MacroTabuleiro()
    for coluna in range(3):
        macro.alteraTabuleiro(1, coluna, "O")
    return macro

@pytest.fixture
def macrotabuleiro_coluna_fechada():
    macro = MacroTabuleiro()
    for linha in range(3):
        macro.alteraTabuleiro(linha, 1, "X")
    return macro

@pytest.fixture
def macrotabuleiro_diagonal_fechada():
    macro = MacroTabuleiro()
    for linha in range(3):
        macro.alteraTabuleiro(linha, linha, "X")
    return macro

@pytest.fixture
def macrotabuleiro_velha():
    velha = MacroTabuleiro()
    velha.defineTabuleiro([["X", "O", "O"], ["O", "O", "X"], ["X", "X", "O"]])
    return velha

class TestaMacroTabuleiro:
    # TESTA O CONSTRUTOR
    def test_init(self):
        macro_tabuleiro = MacroTabuleiro()
        funciona = True
        for linha in range(3):
            for coluna in range(3):
                if type(macro_tabuleiro.tabuleiro[linha][coluna]) != Tabuleiro:
                    funciona = False
        assert funciona == True and type(macro_tabuleiro) == MacroTabuleiro
    
    # TESTA MÉTODO QUE ALTERA O MACRO TABULEIRO
    def test_alteraTabuleiro_macro(self, macrotabuleiro_exemplo):
        macrotabuleiro_exemplo.alteraTabuleiro(0, 0, "O")
        assert macrotabuleiro_exemplo.tabuleiro[0][0] == "O"
    
    # TESTA MÉTODO QUE RETORNA ELEMENTO DO MACRO TABULEIRO
    def test_retornaElemento_macro(self, macrotabuleiro_linha_fechada):
        elemento = macrotabuleiro_linha_fechada.retornaElemento(1,2)
        assert elemento == "O"
    
    # TESTA MÉTODO QUE RETORNA LINHAS DO MACRO TABULEIRO QUE AINDA NÃO FORAM COMPLETAS
    def test_retornaLinhasAbertas_macro(self, macrotabuleiro_exemplo):
        lista = macrotabuleiro_exemplo.retornaLinhasAbertas()
        assert lista == [1, 2, 3]
    
    # TESTA MÉTODO QUE RETORNA COLUNAS DE UMA LINHA DO MACRO TABULEIRO QUE AINDA NÃO FORAM COMPLETAS
    def test_retornaColunasAbertas_macro(self, macrotabuleiro_coluna_fechada):
        lista = macrotabuleiro_coluna_fechada.retornaColunasAbertas(1)
        assert lista == [1, 3]
    
    # TESTAM MÉTODO QUE VERIFICA SE MACRO TABULEIRO JÁ FOI FECHADO
    def test_chegouAoFim_aberto_macro(self, macrotabuleiro_exemplo):
        acabou = macrotabuleiro_exemplo.chegouAoFim()
        assert acabou == 0
    def test_chegouAoFim_jogador1_linha(self, macrotabuleiro_linha_fechada):
        acabou = macrotabuleiro_linha_fechada.chegouAoFim()
        assert acabou == 1
    def test_chegouAoFim_jogador2_diagonal(self, macrotabuleiro_diagonal_fechada):
        acabou = macrotabuleiro_diagonal_fechada.chegouAoFim()
        assert acabou == 2
    def test_chegouAoFim_jogador2_coluna(self, macrotabuleiro_coluna_fechada):
        acabou = macrotabuleiro_coluna_fechada.chegouAoFim()
        assert acabou == 2
    def test_chegouAoFim_velha(self, macrotabuleiro_velha):
        acabou = macrotabuleiro_velha.chegouAoFim()
        assert acabou == -1
    
    # TESTAM MÉTODO QUE RETORNA UM (MICRO) TABULEIRO DE UM MACRO TABULEIRO A PARTIR DO ÍNDICE DADO
    def test_retornaMicro(self, macrotabuleiro_exemplo):
        micro = macrotabuleiro_exemplo.retornaMicro(1)
        assert (type(micro) == Tabuleiro) and (micro.tabuleiro == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
    def test_retornaMicro_errado(self, macrotabuleiro_exemplo):
        micro = macrotabuleiro_exemplo.retornaMicro(-6)
        assert micro == -1


@pytest.fixture
def tabuleiro_numeros_exemplo():
    exemplo = TabuleiroDeNumeros()
    exemplo.alteraTabuleiro(0, 0, "X")
    exemplo.alteraTabuleiro(1, 2, "O")
    exemplo.alteraTabuleiro(2, 1, "X")
    return exemplo

class TestaTabuleiroNumeros:
    # TESTA O CONSTRUTOR
    def test_init(self):
        tabuleiro_numeros = TabuleiroDeNumeros()
        assert tabuleiro_numeros.tabuleiro == [[1,2,3],[4,5,6],[7,8,9]] and type(tabuleiro_numeros) == TabuleiroDeNumeros
    
    # TESTA MÉTODO QUE RETORNA LISTA DE (MICRO) TABULEIROS AINDA NÃO FECHADOS
    def test_retornaListaAbertos(self, tabuleiro_numeros_exemplo):
        lista = tabuleiro_numeros_exemplo.retornaListaAbertos()
        assert lista == [2, 3, 4, 5, 7, 9]


@pytest.fixture
def jogador_exemplo():
    jogador = Jogador()
    jogador.mudaSimbolo("X")
    return jogador

class TestaJogador:
    # TESTA O CONSTRUTOR
    def test_init(self):
        jogador = Jogador()
        assert type(jogador) == Jogador and jogador.simbolo == ""
    
    # TESTA MÉTODO QUE RETORNA O SÍMBOLO DO JOGADOR
    def test_retornaSimbolo(self, jogador_exemplo):
        simbolo = jogador_exemplo.retornaSimbolo()
        assert simbolo == "X"

    # TESTA MÉTODO QUE MUDA O SÍMBOLO DO JOGADOR
    def test_mudaSimbolo(self, jogador_exemplo):
        jogador_exemplo.mudaSimbolo("O")
        assert jogador_exemplo.simbolo == "O"


@pytest.fixture
def humano_exemplo():
    humano = JogadorHumano()
    humano.mudaSimbolo("X")
    return humano

@pytest.fixture
def lista_tabuleiros_exemplo():
    numeros = TabuleiroDeNumeros()
    numeros.alteraTabuleiro(0, 1, "X")
    lista = numeros.retornaListaAbertos()
    return lista

@pytest.fixture
def linhas_abertas_exemplo():
    lista = [1, 3]
    return lista

@pytest.fixture
def colunas_abertas_exemplo():
    lista = [3]
    return lista

class TestaJogadorHumano:
    # TESTA O CONSTRUTOR
    def test_init(self):
        jogador = JogadorHumano()
        assert type(jogador) == JogadorHumano
    
    # TESTAM MÉTODO DE ESCOLHA DO TABULEIRO DO JOGADOR HUMANO
    def test_escolheTabuleiro_fechado(self, lista_tabuleiros_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2")
        escolha = humano_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha == -1
    def test_escolheTabuleiro_inexistente(self, lista_tabuleiros_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "20")
        escolha = humano_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha == -1
    def test_escolheTabuleiro_semResposta(self, lista_tabuleiros_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "")
        escolha = humano_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha == -1
    def test_escolheTabuleiro_valido(self, lista_tabuleiros_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "9")
        escolha = humano_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha == 9
    
    # TESTAM MÉTODO DE ESCOLHA PELO JOGADOR HUMANO DA LINHA NA QUAL FARÁ A JOGADA
    def test_escolheLinha_fechada(self, linhas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2")
        escolha = humano_exemplo.escolheLinha(linhas_abertas_exemplo)
        assert escolha == -1
    def test_escolheLinha_inexistente(self, linhas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "-15")
        escolha = humano_exemplo.escolheLinha(linhas_abertas_exemplo)
        assert escolha == -1
    def test_escolheLinha_estranho(self, linhas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "oi")
        escolha = humano_exemplo.escolheLinha(linhas_abertas_exemplo)
        assert escolha == -1
    def test_escolheLinha_valido(self, linhas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        escolha = humano_exemplo.escolheLinha(linhas_abertas_exemplo)
        assert escolha == 1
    
    # TESTAM MÉTODO DE ESCOLHA PELO JOGADOR HUMANO DA COLUNA NA QUAL FARÁ A JOGADA
    def test_escolheColuna_fechada(self, colunas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        escolha = humano_exemplo.escolheColuna(colunas_abertas_exemplo)
        assert escolha == -1
    def test_escolheColuna_inexistente(self, colunas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1000000000")
        escolha = humano_exemplo.escolheColuna(colunas_abertas_exemplo)
        assert escolha == -1
    def test_escolheColuna_estranho(self, colunas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "tchau")
        escolha = humano_exemplo.escolheColuna(colunas_abertas_exemplo)
        assert escolha == -1
    def test_escolheColuna_valido(self, colunas_abertas_exemplo, humano_exemplo, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "3")
        escolha = humano_exemplo.escolheColuna(colunas_abertas_exemplo)
        assert escolha == 3


@pytest.fixture
def aleatorio_exemplo():
    aleatorio = JogadorAleatorio()
    aleatorio.mudaSimbolo("X")
    return aleatorio

class TestaJogadorAleatorio:
    # TESTA O CONSTRUTOR
    def test_init(self):
        jogador = JogadorAleatorio()
        assert type(jogador) == JogadorAleatorio
    
    # TESTA MÉTODO QUE RETORNA O TABULEIRO ESCOLHIDO PELO JOGADOR ALEATÓRIO
    def test_escolheTabuleiro(self, lista_tabuleiros_exemplo, aleatorio_exemplo):
        random.seed(10)
        escolha1 = random.choice(lista_tabuleiros_exemplo)
        random.seed(10)
        escolha2 = aleatorio_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha1 == escolha2 and escolha2 in range(1,10)
    
    # TESTA MÉTODO QUE RETORNA A LINHA ESCOLHIDA PELO JOGADOR ALEATÓRIO
    def test_escolheLinha(self, tabuleiro_preenchido, aleatorio_exemplo):
        linhas_abertas = tabuleiro_preenchido.retornaLinhasAbertas()
        escolha = aleatorio_exemplo.escolheLinha(linhas_abertas)
        assert escolha == 2

    # TESTA MÉTODO QUE RETORNA A COLUNA ESCOLHIDA PELO JOGADOR ALEATÓRIO
    def test_escolheColuna(self, tabuleiro_preenchido, aleatorio_exemplo):
        colunas_abertas = tabuleiro_preenchido.retornaColunasAbertas(1)
        escolha = aleatorio_exemplo.escolheColuna(colunas_abertas)
        assert escolha == 2


@pytest.fixture
def comecru_exemplo():
    comecru = JogadorComeCru()
    comecru.mudaSimbolo("O")
    return comecru

class TestaJogadorComeCru:
    # TESTA O CONSTRUTOR
    def test_init(self):
        jogador = JogadorComeCru()
        assert type(jogador) == JogadorComeCru
    
    # TESTA MÉTODO QUE RETORNA O TABULEIRO ESCOLHIDO PELO JOGADOR COME-CRU
    def test_escolheTabuleiro(self, lista_tabuleiros_exemplo, comecru_exemplo):
        escolha = comecru_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo)
        assert escolha == 1
    
    # TESTA MÉTODO QUE RETORNA A LINHA ESCOLHIDA PELO JOGADOR COME-CRU
    def test_escolheLinha(self, tabuleiro_exemplo, comecru_exemplo):
        linhas_abertas = tabuleiro_exemplo.retornaLinhasAbertas()
        escolha = comecru_exemplo.escolheLinha(linhas_abertas)
        assert escolha == 1

    # TESTA MÉTODO QUE RETORNA A COLUNA ESCOLHIDA PELO JOGADOR COME-CRU
    def test_escolheColuna(self, tabuleiro_exemplo, comecru_exemplo):
        colunas_abertas = tabuleiro_exemplo.retornaColunasAbertas(0)
        escolha = comecru_exemplo.escolheColuna(colunas_abertas)
        assert escolha == 1


@pytest.fixture
def inteligente_exemplo():
    inteligente = JogadorInteligente()
    inteligente.mudaSimbolo("O")
    return inteligente

@pytest.fixture
def tabuleiro0():
    tabuleiro = Tabuleiro()
    return tabuleiro

@pytest.fixture
def tabuleiro1():
    tabuleiro = Tabuleiro()
    tabuleiro.defineTabuleiro([["X", "O", " "], [" ", "X", " "], [" ", " ", " "]])
    return tabuleiro

@pytest.fixture
def tabuleiro2():
    tabuleiro = Tabuleiro()
    tabuleiro.defineTabuleiro([["X", "O", " "], [" ", "X", " "], ["X", " ", " "]])
    return tabuleiro

@pytest.fixture
def tabuleiro3():
    tabuleiro = Tabuleiro()
    tabuleiro.defineTabuleiro([[" ", "X", "O"], ["X", " ", " "], ["O", " ", "X"]])
    return tabuleiro

@pytest.fixture
def tabuleiro4():
    tabuleiro = Tabuleiro()
    tabuleiro.defineTabuleiro([[" ", "X", "O"], ["X", "X", " "], ["O", " ", "X"]])
    return tabuleiro

class TestaJogadorInteligente:
    # TESTA O CONSTRUTOR
    def test_init(self):
        jogador = JogadorInteligente()
        assert type(jogador) == JogadorInteligente
    
    # TESTAM MÉTODO QUE RETORNA O TABULEIRO ESCOLHIDO PELO JOGADOR INTELIGENTE
    def test_escolheTabuleiro_aberto(self, lista_tabuleiros_exemplo, inteligente_exemplo):
        ultimo_tabuleiro = 8
        escolha = inteligente_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo, ultimo_tabuleiro)
        assert escolha == 8
    def test_escolheTabuleiro_fechado(self, lista_tabuleiros_exemplo, inteligente_exemplo):
        ultimo_tabuleiro = 2
        escolha = inteligente_exemplo.escolheTabuleiro(lista_tabuleiros_exemplo, ultimo_tabuleiro)
        assert escolha == 1
    
    # TESTAM MÉTODO QUE RETORNA A LINHA ESCOLHIDA PELO JOGADOR INTELIGENTE
    def test_escolheLinha_vazio(self, tabuleiro0, inteligente_exemplo):
        linha = inteligente_exemplo.escolheLinha(tabuleiro0)
        assert linha == 1
    def test_escolheLinha_linhas(self, tabuleiro1, inteligente_exemplo):
        linha = inteligente_exemplo.escolheLinha(tabuleiro1)
        assert linha == 3
    def test_escolheLinha_colunas(self, tabuleiro2, inteligente_exemplo):
        linha = inteligente_exemplo.escolheLinha(tabuleiro2)
        assert linha == 3
    def test_escolheLinha_diagonais(self, tabuleiro3, inteligente_exemplo):
        linha = inteligente_exemplo.escolheLinha(tabuleiro3)
        assert linha == 2
    def test_escolheLinha_semsolucao(self, tabuleiro4, inteligente_exemplo):
        linha = inteligente_exemplo.escolheLinha(tabuleiro4)
        assert linha == 1
    
    # TESTAM MÉTODO QUE RETORNA A COLUNA ESCOLHIDA PELO JOGADOR INTELIGENTE
    def test_escolheColuna_vazio(self, tabuleiro0, inteligente_exemplo):
        inteligente_exemplo.escolheLinha(tabuleiro0)
        coluna = inteligente_exemplo.escolheColuna(tabuleiro0)
        assert coluna == 3
    def test_escolheColuna_linhas(self, tabuleiro1, inteligente_exemplo):
        inteligente_exemplo.escolheLinha(tabuleiro1)
        coluna = inteligente_exemplo.escolheColuna(tabuleiro1)
        assert coluna == 3
    def test_escolheColuna_colunas(self, tabuleiro2, inteligente_exemplo):
        inteligente_exemplo.escolheLinha(tabuleiro2)
        coluna = inteligente_exemplo.escolheColuna(tabuleiro2)
        assert coluna == 3
    def test_escolheColuna_diagonais(self, tabuleiro3, inteligente_exemplo):
        inteligente_exemplo.escolheLinha(tabuleiro3)
        coluna = inteligente_exemplo.escolheColuna(tabuleiro3)
        assert coluna == 2
    def test_escolheColuna_semsolucao(self, tabuleiro4, inteligente_exemplo):
        inteligente_exemplo.escolheLinha(tabuleiro4)
        coluna = inteligente_exemplo.escolheColuna(tabuleiro4)
        assert coluna == 1


@pytest.fixture
def alternador_modo1():
    alternador = AlternadorDeJogadores(1)
    return alternador

@pytest.fixture
def alternador_modo2():
    alternador = AlternadorDeJogadores(2)
    return alternador

class TestaAlternadorDeJogadores:
    # TESTA O CONSTRUTOR
    def test_init(self):
        alternador = AlternadorDeJogadores(1)
        assert type(alternador) == AlternadorDeJogadores and alternador.modo == 1
    
    # TESTA MÉTODO QUE DEFINE O JOGADOR QUE COMEÇA JOGANDO
    def test_defineQuemComeca(self, alternador_modo1):
        random.seed(10)
        resposta = random.randint(0,1)
        random.seed(10)
        comeca = alternador_modo1.defineQuemComeca()
        assert comeca == resposta
    
    # TESTA MÉTODO QUE DEFINE O JOGADOR QUE COMEÇA JOGANDO
    def test_alternaJogador_modo1_0(self, alternador_modo1):
        atual = alternador_modo1.alternaJogador(0)
        assert atual == 1
    def test_alternaJogador_modo1_1(self, alternador_modo1):
        atual = alternador_modo1.alternaJogador(1)
        assert atual == 0
    def test_alternaJogador_modo2(self, alternador_modo2):
        random.seed(10)
        resposta = random.randint(0,1)
        random.seed(10)
        atual = alternador_modo2.alternaJogador(1)
        assert atual == resposta


@pytest.fixture
def jogo_exemplo_inicial():
    jogo = JogoDaVelha_Ultimate()
    return jogo

@pytest.fixture
def jogo_exemplo_1():
    jogo = JogoDaVelha_Ultimate()
    jogo.macro_tabuleiro.retornaMicro(0).defineTabuleiro([["X", " ", "X"], ["O", " ", "O"], ["X", " ", "O"]])
    return jogo

@pytest.fixture
def jogo_exemplo_2():
    jogo = JogoDaVelha_Ultimate()
    jogo.macro_tabuleiro.retornaMicro(8).defineTabuleiro([["X", "X", "X"], ["X", "O", "O"], ["O", "O", "X"]])
    # os jogadores devem ser criados para que o método atualizaMacro() seja testado
    jogo.jogadores = ["", ""]
    jogo.jogadores[0] = Jogador()
    jogo.jogadores[0].mudaSimbolo("O")
    jogo.jogadores[1] = Jogador()
    jogo.jogadores[1].mudaSimbolo("X")
    return jogo

@pytest.fixture
def jogo_exemplo_3():
    jogo = JogoDaVelha_Ultimate()
    jogo.macro_tabuleiro.retornaMicro(3).defineTabuleiro([["O", " ", " "], ["X", "O", "O"], [" ", "X", "O"]])
    # os jogadores devem ser criados para que o método atualizaMacro() seja testado
    jogo.jogadores = ["", ""]
    jogo.jogadores[0] = Jogador()
    jogo.jogadores[0].mudaSimbolo("O")
    jogo.jogadores[1] = Jogador()
    jogo.jogadores[1].mudaSimbolo("X")
    return jogo

@pytest.fixture
def jogo_exemplo_4():
    jogo = JogoDaVelha_Ultimate()
    jogo.macro_tabuleiro.retornaMicro(7).defineTabuleiro([["O", "X", "X"], ["X", "O", "O"], ["O", "X", "X"]])
    # os jogadores devem ser criados para que o método atualizaMacro() seja testado
    jogo.jogadores = ["", ""]
    jogo.jogadores[0] = Jogador()
    jogo.jogadores[0].mudaSimbolo("O")
    jogo.jogadores[1] = Jogador()
    jogo.jogadores[1].mudaSimbolo("X")
    return jogo

class TestaJogoDaVelha_Ultimate:
    # TESTA O CONSTRUTOR
    def test_init(self, jogo_exemplo_inicial):
        assert type(jogo_exemplo_inicial.macro_tabuleiro) == MacroTabuleiro and type(jogo_exemplo_inicial.lista_tabuleiros) == TabuleiroDeNumeros
        assert jogo_exemplo_inicial.ultimo_tabuleiro_jogado == -1 and jogo_exemplo_inicial.num_rodadas == 0 and type(jogo_exemplo_inicial) == JogoDaVelha_Ultimate
    
    # TESTAM MÉTODO QUE CRIA OS JOGADORES (foi possível testar apenas com dois tipos iguais, porém o código
    # do método deixa evidente que, testado para dois tipos iguais, o para dois diferentes é trivial).
    def test_criaJogadores_humanos(self, jogo_exemplo_inicial, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        jogo_exemplo_inicial.criaJogadores()
        assert type(jogo_exemplo_inicial.jogadores[0]) == JogadorHumano and type(jogo_exemplo_inicial.jogadores[1]) == JogadorHumano
    def test_criaJogadores_aleatorios(self, jogo_exemplo_inicial, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        jogo_exemplo_inicial.criaJogadores()
        assert type(jogo_exemplo_inicial.jogadores[0]) == JogadorAleatorio and type(jogo_exemplo_inicial.jogadores[1]) == JogadorAleatorio
    def test_criaJogadores_comecru(self, jogo_exemplo_inicial, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "2")
        jogo_exemplo_inicial.criaJogadores()
        assert type(jogo_exemplo_inicial.jogadores[0]) == JogadorComeCru and type(jogo_exemplo_inicial.jogadores[1]) == JogadorComeCru
    def test_criaJogadores_inteligentes(self, jogo_exemplo_inicial, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "3")
        jogo_exemplo_inicial.criaJogadores()
        assert type(jogo_exemplo_inicial.jogadores[0]) == JogadorInteligente and type(jogo_exemplo_inicial.jogadores[1]) == JogadorInteligente

    # TESTAM MÉTODO QUE ATUALIZA MACRO TABULEIRO SE ALGUMA CASA TIVER SIDO FECHADA
    def test_atualizaMacro_aberto(self, jogo_exemplo_1):
        indice = 0
        micro_tabuleiro = jogo_exemplo_1.macro_tabuleiro.retornaMicro(indice)
        retorno = jogo_exemplo_1.atualizaMacro(micro_tabuleiro, indice)
        assert retorno == None and type(jogo_exemplo_1.macro_tabuleiro.retornaMicro(indice)) == Tabuleiro
    def test_atualizaMacro_jogador2(self, jogo_exemplo_2):
        indice = 8
        micro_tabuleiro = jogo_exemplo_2.macro_tabuleiro.retornaMicro(indice)
        retorno = jogo_exemplo_2.atualizaMacro(micro_tabuleiro, indice)
        assert retorno == None and jogo_exemplo_2.macro_tabuleiro.retornaMicro(indice) == "X"
    def test_atualizaMacro_jogador1(self, jogo_exemplo_3):
        indice = 3
        micro_tabuleiro = jogo_exemplo_3.macro_tabuleiro.retornaMicro(indice)
        retorno = jogo_exemplo_3.atualizaMacro(micro_tabuleiro, indice)
        assert retorno == None and jogo_exemplo_3.macro_tabuleiro.retornaMicro(indice) == "O"
    def test_atualizaMacro_velha(self, jogo_exemplo_4):
        indice = 7
        micro_tabuleiro = jogo_exemplo_4.macro_tabuleiro.retornaMicro(indice)
        random.seed(10)
        sorteado = random.randint(1,2)
        random.seed(10)
        retorno = jogo_exemplo_4.atualizaMacro(micro_tabuleiro, indice)
        assert retorno == None and jogo_exemplo_4.macro_tabuleiro.retornaMicro(indice) == jogo_exemplo_4.jogadores[sorteado-1].retornaSimbolo()