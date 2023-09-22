''' Esse é o arquivo principal, ele será responssável por receber os comandos no display que ocorrer durante o jogo '''

import pygame as p
from ChessEngine import *

WIDTH = HEIGHT = 512  # Outra opção seria a resolução de 400 para melhor qualidade
DIMENSION = 8  # Tamanho da Tábua é 8x8
SQ_SIZE = HEIGHT // DIMENSION  # O Tamanho do quadrado será responsivo à resolução
MAX_FPS = 15  # Para futuras animações
IMAGES = {}


'''
Para melhor desempenho, é necessário que as imagens sejam alocadas na memória apenas uma vez no arquivo principal
'''


def loadImages():
    pieces = ['bT', 'bC', 'bB', 'bR', 'bK',
              'bP', 'wT', 'wC', 'wB', 'wR', 'wK', 'wP']

    for piece in pieces:
        # 'transform.scale' está redimencionando a imagem mantedo a qualidade passando o parâmetro do tamanho que é N²
        IMAGES[piece] = p.transform.scale(p.image.load(
            "pecas/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Nota: Observe que dessa forma estamos salvando todas as imagens no dicionário de *IMAGES*


'''
O arquivo principal do projeto, ele irá dar conta da rederização e atualização das imagens
'''


def main():

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))  # Criando a tela do jogo
    clock = p.time.Clock()  # Relógio do jogo
    screen.fill(p.Color("white"))
    gs = GameState()
    loadImages()  # As imagens é chamada apenas uma vez antes do loop
    running = True  # condição para o loop da tela
    sqSelected = ()  # Armazena a casa que o usuário clicar, (Tupla: (linha, coluna))
    # mantem armazenado os clicks do usuário (duas tulplas: [(6,4),(4,4)])
    playerClicks = []

    while running:

        for e in p.event.get():

            if e.type == p.QUIT:  # Evento de sair
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:  # Evento de click do mouse
                location = p.mouse.get_pos()  # captura a posição do mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE

                if sqSelected == (row, col):  # o usuário clickou nas mesmas casas
                    sqSelected = ()
                    playerClicks = []  # retira o click do player

                else:
                    sqSelected = (row, col)
                    # Adicionando o primeiro e segundo click do usuário
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2:
                    if gs.board[playerClicks[0][0]][playerClicks[0][1]] == '--':
                        sqSelected = ()
                        playerClicks = []
                    else:
                        move = gs.Move(
                            playerClicks[0], playerClicks[1], gs.board)
                        gs.makemove(move)
                        sqSelected = ()  # reseta a seleção
                        playerClicks = []  # resetando os clicks

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsável por todos os desenhos com e interações
'''


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


'''
# Desenha os quadrados na tábua
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):

            '''
            levando em consideração que o r(linha) na posição 0 e o r na posição 1 irão dar restos diferentes quando forem 
            comparado com o c(coluna) na posição zero por exemplo. Então abaixo temos a seleção das cores mediante o que for o 
            resultado do resto
            '''

            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
desenha as peças em cima dos quadrados
'''


def drawPieces(screen, board):

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':  # casa não Não está vazia
                screen.blit(IMAGES[piece], p.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
