''' Essa classe é a responsável por guardar toda a informação sobre o estado atual do jogo, 
e também é responsável por determinar os movimentos válidos do jogo '''


class GameState():
    def __init__(self) -> None:

        # A tábua é possui lista de 8x8 e cada casa possui um elemento de dois caractere
        # O primeiro caractere representa a cor da peça "W" para white(Branco) e "B" para Black(Preto)
        # O segundo caractere representa o tipo da peça nas seguinte ordem: Torre, Cavalo, Bispo, Rainha, Rei, Bispo, Cavalo, Torre
        # '--' significa espaço vazio

        self.board = [
            ['bT', 'bC', 'bB', 'bK', 'bR', 'bB', 'bC', 'bT'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wT', 'wC', 'wB', 'wK', 'wR', 'wB', 'wC', 'wT'],
        ]

        self.whiteToMove = True
        self.moveLog = []

    def makemove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # armazenando os movimentos gerados pelos jogadores
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # trocar os jogadores

    class Move():

        # Numerando as linhas e colunas de 1 a 8
        ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                       "5": 3, "6": 2, "7": 1, "1": 0}
        rowsToRank = {v:k for k, v in ranksToRows.items()}

        # Mapeando as colunas de A a H
        filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                       "e": 4, "f": 5, "g": 6, "h": 7}
        colsToFile = {v:k for k, v in filesToCols.items()}

        def __init__(self, startSq, endSq, board):

            self.startRow = startSq[0]
            self.startCol = startSq[1]
            self.endRow = endSq[0]
            self.endCol = endSq[1]

            # Onde a peça estava
            self.pieceMoved = board[self.startRow][self.startCol]
            # Onde a peça será movida
            self.pieceCaptured = board[self.endRow][self.endCol]

        def getChessNotation(self):
            # Essa função retorna a posição da casa e da coluna
            return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endRow)

        def getRankFile(self, r, c):
            return self.colsToFile[c] + self.rowsToRank[r]
