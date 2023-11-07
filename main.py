import django
from model import *

if __name__ == '__main__':
    model = Model('localhost', 'root', 'TheHateUGive13$', 'sudoku')

    game = model.databaseToMatrix("game")
    solutionToGame = model.databaseToMatrix("solution")

    model.addNumber(game, solutionToGame, 5, 0, 2)

    print(game)
