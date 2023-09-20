''' Esse é o arquivo principal, ele será repsonssável por receber os comandos no display que ocorrer durante o jogo '''

from ChessMain import *

WIDTH = HEIGHT = 512 # Outra opção seria a resolução de 400 para melhor qualidade
DIMENSION = 8 # Tamanho da Tábua é 8x8
SQ_SIZE = HEIGHT // DIMENSION # O Tamanho do quadrado será responsivo à resolução
MAX_FPS = 15 # Para futuras animações
IMAGES = {}

'''
Para melhor desempenho é necessário que as imagens sejam alocadas na memória apenas uma vez no arquivo principal
'''

def loadImages():
    pieces = ['bT', 'bC', 'bB', 'bR', 'bK','wT', 'wC', 'wB', 'wR', 'wK','wP']
    
    for piece in pieces:
        IMAGES[piece] = p.image.load("pecas/"+ piece +".png")

    # Nota: Observe que dessa forma estamos salvando todas as imagens no dicionário de *IMAGES*