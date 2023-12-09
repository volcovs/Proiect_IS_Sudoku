import mysql.connector
import random

class Model_Sudoku():
    def __init__(self, host, user, password, db_name):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=3306,
            database=db_name
        )
        self.firstBoard = [
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]
             ]


    def newGame(self):
        # method for continuing the game already present in database
        m = []

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM game LIMIT 1')

        # lista de tuple (id, difficulty, row1, row2 .. row9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(2, 11):
                m.append(e[i])

        board = m
        return m


    def newGameSolution(self):
        m = []

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM solution LIMIT 1')

        # lista de tuple (id, difficulty, row1, row2 .. row9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(3, 12):
                m.append(e[i])

        board = m
        return m


    def checkCorrectIneff(self, m, solution):
        matrix1 = [e.split(",") for e in m]
        matrix2 = [e.split(",") for e in solution]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] != '0' and matrix1[i][j] != matrix2[i][j]:
                    return False, i, j

        return True, 0, 0

    def updateDatabase(self, m):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM solution LIMIT 1')

        # lista de tuple (id, difficulty, row1, row2 .. row9)
        all_data = cursor.fetchall()

        for e in all_data:
            id = e[0]

        for i in range(0, 9):
            cursor.execute('UPDATE game SET col' + str(i+1) + ' = "' + m[i] + '" WHERE id = ' + str(id) + ';')

        self.db.commit()


    def abortGame(self):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM solution')
        cursor.execute('DELETE FROM game')
        self.db.commit()


    # the board generating methods
    def findEmpty(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    return y, x  # y = row , x = column
        # if we got here it mean that we finish the sudoku, so return none
        return None

    def validCheck(self, board, number, coordinates):
        # checking row
        for x in range(len(board[0])):
            if number == board[coordinates[0]][x] and coordinates[1] != x:  # coordinates[0]= row
                return False

        # checking column
        for y in range(len(board)):
            if number == board[y][coordinates[1]] and coordinates[0] != y:
                return False

        # checking the box
        box_x = coordinates[1] // 3
        box_y = coordinates[0] // 3

        for y in range(box_y * 3, box_y * 3 + 3):
            for x in range(box_x * 3, box_x * 3 + 3):
                if number == board[y][x] and (y, x) != coordinates:
                    return False

        return True

    def generateRandomBoard(self, board):
        # end condition:- getting to the end of the board - the function findEmpty return NONE
        find = self.findEmpty(board)
        if find is None:  # if find != False
            return True
        else:
            row, col = find
        for number in range(1, 10):
            randomNumber = random.randint(1, 9)
            if self.validCheck(board, randomNumber, (row, col)):
                board[row][col] = randomNumber
                if self.generateRandomBoard(board):
                    return True

                board[row][col] = 0
        return False

    def deleteCells(self, firstBoard, number):
        while number:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if firstBoard[row][col] != 0:
                firstBoard[row][col] = 0
                number = number - 1

    def generateLevel(self, difficulty):
        self.abortGame()
        self.generateRandomBoard(self.firstBoard)
        cursor = self.db.cursor()

        if difficulty == "Easy":
            # update database, solution table
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES (1, "easy", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
            self.deleteCells(self.firstBoard, 30)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES ("easy", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
        elif difficulty == "Medium":
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES (1, "medium", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
            self.deleteCells(self.firstBoard, 35)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES ("medium", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
        else:
            # difficulty == "Hard" or invalid
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES (1, "hard", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
            self.deleteCells(self.firstBoard, 40)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9)'
                ' VALUES ("hard", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '");')
            self.db.commit()
