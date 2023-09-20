''' Essa classe é a responsável por guardar toda a informação sobre o estado atual do jogo, 
e também é responsável por determinar os movimentos válidos do jogo '''


class GameState():
    def __init__(self) -> None:

        # A tábua é possui lista de 8x8 e cada casa possui um elemento de dois caractere
        # O primeiro caractere representa a cor da peça "W" para white e "B" para Black
        # O segundo caractere representa o tipo da peça nas seguinte ordem: Torre, Cavalo, Bispo, Rainha, Rei, Bispo, Cavalo, Torre
        # '--' significa espaço vazio

        self.board = [
            ['bT', 'bC', 'bB', 'bR', 'bK', 'bB', 'bC', 'bT'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wT', 'wC', 'wB', 'wR', 'wK', 'wB', 'wC', 'wT'],
        ]

        self.whiteToMove = True
        self.moveLog = []
