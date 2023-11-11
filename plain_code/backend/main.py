import django
from model import *

if __name__ == '__main__':
    # simple main to test the Python functions
    model = Model('localhost', 'root', 'pass', 'sudoku')

    game = model.newGame()
    solutionToGame = model.newGameSolution()

    model.addNumber(game, solutionToGame, 5, 0, 2)

    print(game)
