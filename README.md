# EP4-MAC0216
### Repositório para o Exercício Programa 4 (final) de Técnicas de Programação I (MAC0216).

## INTRODUÇÃO
Este projeto compõe o Exercício-Programa 4, pertencente à disciplina MAC0216 (Técnicas de Programação I), a qual é ministrada pelo docente Fabio Kon e de responsabilidade do IME-USP. De maneira geral, o projeto visa a verificar conceitos de programação mais aprofundada em Python, com enfoque especial em **Programação Orientada a Objetos**, voltada para o desenvolvimento de classes que permitam a criação de um jogo-da-velha diferenciado (*Ultimate Tic-Tac-Toe*). O projeto envolveu a participação de:

‣ Matheus Sanches Jurgensen (NUSP: 12542199)
‣ Caio Rodrigues Gama (NUSP: 12543381)

## OBJETIVO
O objetivo do projeto foi, como já dito, verificar conceitos de Programação Orientada a Objetos em Python. Devia-se criar um jogo, chamado de **Jogo da Velha Ultimate**. A execução desse jogo devia ser integralmente baseada no uso de classes (com responsabilidade única) e seus objetos, havendo o máximo possível de reutilização de código, além da aplicação de conteúdos como herança e polimorfismo. Além disso, buscou-se praticar a criação de um arquivo de testes das classes e seus métodos, utilizando o *PyTest*, para verificar, por meio dos testes automatizados, o correto funcionamento de todo o código para os mais diversos casos.

## SOBRE O DIRETÓRIO
Neste diretório do GitHub ([link](https://github.com/mathjug/EP4-MAC0216)), encontram-se alguns arquivos de maior importância para o correto funcionamento e entendimento do jogo. Esses arquivos são os seguintes:

1. JogodaVelha.py: é o arquivo principal do projeto, composto por todo o código necessário para o funcionamento do jogo. Ele é composto por 10 diferentes classes (sendo que algumas utilizam do conceito de herança, enquanto outras não), com seus diversos métodos. De maneira geral, essas classes objetivam abstrair conceitos como os diferentes tipos de tabuleiros e jogadores existentes, além de um mecanismo que alterna a qual jogador pertence a próxima jogada, e, por fim, uma classe que abstrai o jogo de maneira geral, com seus métodos fundamentais.

2. test_JogodaVelha.py: é o arquivo de teste de *JogodaVelha.py*. Ele utiliza do ferramental disponibilizado pelo *PyTest* para testar todas as 10 classes. Testa-se o máximo de métodos que são possíveis, inclusive alguns que dependem de respostas do usuário pelo terminal. No entanto, alguns métodos são de muito difícil testagem, seja porque executam o loop do jogo como um todo, seja porque apenas realizam a chamada de outros métodos. Por isso, esses métodos em específico não são testados. No entanto, isso não diminui em nada a absoluta certeza de que o programa funciona corretamente, visto que são funções com comportamentos amplamente previsíveis, sem nenhuma lógica complexa por trás, e que chamam métodos que, por sua vez, são, sim, testados. Para que esse programa, que contém uma bateria de testes automatizados, funcione corretamente, ele deve estar localizado no mesmo diretório local de *JogodaVelha.py*.

3. README.md: é este presente arquivo, que contém todas as instruções para a correta execução do jogo e seus testes. Além disso, contém todas as regras do jogo (*Ultimate Tic-Tac-Toe*).

## MODO DE EXECUÇÃO
Para que se possa executar adequadamente o jogo, o procedimento é simples e sucinto:

1) Faça download dos arquivos do diretório do GitHub para seu computador. Caso esses arquivos venham compactados em um arquivo de tipo ZIP, extraia-o para algum diretório local desejado. Nele, uma nova pasta será criada, contendo todos os arquivos encontrados no GitHub.

2) No terminal, mova-se para essa pasta local.

3) Agora, basta executar o jogo. Essa execução depende de que o usuário tenha Python instalado em seu computador. Caso não o tenha, faça a sua instalação (cujos procedimentos são muito fáceis e podem ser rapidamente encontrados na internet). Para executar, digite, no terminal, "python JogodaVelha.py". Esse comando pode variar de acordo com a versão de Python instalada. Em alguns casos, pode ser necessário digitar "python3 JogodaVelha.py" ou alguma variação similar a essa. Por isso, descubra qual forma o Python instalado em seu computador exige.

## REGRAS DO JOGO
Agora, resta esclarecer quais as regras do jogo e o modo de jogá-lo. Basicamente, ele é composto por um tabuleiro de jogo da velha comum (macro tabuleiro), mas que contém, em cada uma de suas nove casas, um novo tabuleiro de jogo da velha (micro tabuleiros). Esses 9 micro tabuleiros são idênticos aos comuns em jogos da velha e seguem as mesmas regras. No entanto, caso ocorra velha em um deles, é feito um sorteio para definir quem é o seu vencedor (jogada de uma moeda). Para definir, por sua vez, quem venceu no macro tabuleiro (e, portanto, no jogo como um todo), é necessária uma melhor explicação sobre as regras do jogo no geral:

### TIPOS DE JOGADORES
--> Primeiramente, será necessário escolher quais serão os tipos dos dois jogadores que participarão do jogo. Os jogadores podem ser de tipos iguais ou diferentes. São, no total, 4 tipos, mudando a forma como escolhem em qual tabuleiro e em qual posição jogar:

1. HUMANO: jogador controlado por um ser humano real. As jogadas são definidas a partir de chamadas ao jogador no terminal.
2. ALEATÓRIO: jogador automático que define suas jogadas (micro tabuleiro e posição) de maneira completamente aleatória.
3. COME-CRU: jogador automático que joga no primeiro tabuleiro disponível, e, nele, na primeira posição disponível.
4. INTELIGENTE: jogador automático implementado como uma Inteligência Artificial. Para definir em qual micro tabuleiro fará sua jogada, repete o mesmo escolhido pelo último jogador a jogar. No entanto, existem casos em que isso não é possível. Primeiramente, caso o jogador inteligente esteja fazendo a primeira jogada de todas (a jogada inicial), ela ocorre na primeira posição do primeiro tabuleiro. Em segundo lugar, caso o jogador não seja o primeiro, mas o tabuleiro em que foi feita a última jogada tenha sido fechado, ele escolhe o primeiro micro tabuleiro disponível no macro tabuleiro. Uma vez que isso tenha sido definido, resta agora escolher em qual posição jogar. Basicamente, o jogador faz uma busca por uma posição promissora (ou seja, que pode levar a uma possível vitória no micro tabuleiro). Essa busca é iniciada pelas linhas, depois pelas colunas e, por fim, pelas diagonais (primeiro a principal). Caso não haja uma posição promissora no micro tabuleiro escolhido, a jogada é feita na sua primeira posição disponível.

### MODOS DE ALTERNÂNCIA DE JOGADORES
--> Em seguida, será solicitado o modo como ocorrerá a alternância de jogadores (definição de quem é o próximo a jogar). São dois modos disponíveis:

1. ALTERNADO SIMPLES: um jogador nunca faz duas jogadas seguidas. Ou seja, quando um jogador faz a jogada atual, o outro fará a próxima.
2. ALEATÓRIO: a cada jogada, define-se quem joga de maneira aleatória. Ou seja, pode ocorrer de um jogador fazer jogadas seguidas.

### SORTEIO INICIAL
--> Então, ocorrerá um sorteio para definir quem fará a primeira jogada.

### FAZENDO A JOGADA
--> Para que seja definida a jogada do jogador atual, o programa solicita, primeiramente, que ele escolha um tabuleiro válido para jogar (identificados de 1 a 9). A resposta é obtida de acordo com o tipo do jogador. Caso ele seja um usuário humano e selecione um tabuleiro fechado ou inexistente, o jogo não aceita a resposta e solicita que seja dada uma válida.

--> Em seguida, o jogador deve escolher em qual linha jogar, dentre as válidas exibidas pelo jogo. Mais uma vez, essa escolha é feita segundo os critérios definidos para cada tipo de jogador, e, caso um usuário humano selecione uma linha inválida, o jogo a rejeita e solicita uma válida.

--> Por fim, dados o tabuleiro e a linha de jogada, resta agora definir em qual coluna jogar. Mais uma vez, o jogo exibe quais as colunas da linha escolhida que estão disponíveis, e o jogador faz essa escolha de acordo com os critérios do seu tipo. Caso um jogador humano selecione uma coluna inválida, o jogo solicita uma nova coluna, porém válida.

### VENCENDO O JOGO
--> Como já dito, o objetivo do jogo é vencer, segundo as regras comuns do jogo da velha, no macro tabuleiro. Para que isso ocorra, sempre que um micro tabuleiro é vencido por um jogador, a posição correspondente a ele é definida como pertencente ao jogador que o venceu. Caso ocorra velha em um micro tabuleiro, um sorteio define a quem ele pertencerá. Assim, vence o jogo quem possuir primeiro todas as posições de alguma linha, coluna ou diagonal do macro tabuleiro. Pode acontecer, no entanto, que ocorra velha nele, definindo, assim, um empate.

## OBSERVAÇÕES
Como já indicado e explicado acima, este grupo implementou dois bônus no jogo. Primeiramente, desenvolveu-se uma **Inteligência Artificial** como um tipo de jogador complementar. Ademais, o outro bônus implementado foi a opção de escolha de um modo aleatório de alternância de jogadores (*Random Turn Tic-Tac-Toe*).