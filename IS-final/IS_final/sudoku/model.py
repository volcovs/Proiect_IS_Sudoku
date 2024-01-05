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

    def getUserFromDatabase(self, username, password):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = "' + username + '" AND pass = "' + password + '";')

        user = cursor.fetchall()
        if len(user) == 0:
            return "anon"

        # return the username stored in the database
        return user[0][1]

    def getAllUserData(self, username):
        # presumably, the user has already logged in and there is no need to check the password
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = "' + username + '";')

        user = cursor.fetchall()
        # return the user data as a list
        return user

    def addNewUserToDatabase(self, user_data):
        cursor = self.db.cursor()

        cursor.execute(
            'INSERT INTO users(username, first_name, last_name, pass, games_won, games_started, total_time, best_time) VALUES ("'
            + user_data['username'] + '", "' + user_data['first_name'] + '", "' + user_data['last_name'] + '", "'
            + user_data['password'] + '", ' + str(user_data['games_won']) + ', ' + str(user_data['games_total']) + ', "' + user_data['time_total'] + '", "'
            + user_data['best_time'] + '");')

        self.db.commit()

    def newGame(self, username):
        # method for continuing the game already present in database
        m = []

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM game, users WHERE username = "' + username + '" AND user_id = users.id;')

        # lista de tuple (id, difficulty, col1, col2 ... col9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(2, 11):
                m.append(e[i])

        return m

    def newGameSolution(self, username):
        m = []

        cursor = self.db.cursor()
        cursor.execute(
            'SELECT solution.id, solution.id_game, solution.difficulty, solution.col1, solution.col2, solution.col3, solution.col4, solution.col5, solution.col6, solution.col7, solution.col8,' +
            'solution.col9 FROM game, solution, users WHERE username = "' + username + '" AND solution.user_id = users.id AND id_game = game.id;')

        # lista de tuple (id, difficulty, col1, col2 ... col9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(3, 12):
                m.append(e[i])

        return m

    def getHint(self, m, solution):
        matrix1 = [e.split(",") for e in m]
        matrix2 = [e.split(",") for e in solution]

        i = random.randint(0, len(matrix1) - 1)
        j = random.randint(0, len(matrix1) - 1)
        while matrix1[i][j] != '0':
            i = random.randint(0, len(matrix1) - 1)
            j = random.randint(0, len(matrix1) - 1)

        return [matrix2[i][j], i, j]

    def checkCorrectIneff(self, m, solution):
        matrix1 = [e.split(",") for e in m]
        matrix2 = [e.split(",") for e in solution]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] != '0' and matrix1[i][j] != matrix2[i][j]:
                    return False, i, j

        return True, 0, 0

    def checkVictory(self, m, solution):
        matrix1 = [e.split(",") for e in m]
        matrix2 = [e.split(",") for e in solution]

        if (not matrix1) or (not matrix2):
            return False

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] == '0':
                    return False
                if matrix1[i][j] != '0' and matrix1[i][j] != matrix2[i][j]:
                    return False

        return True

    def updateDatabase(self, m, username):
        cursor = self.db.cursor()
        cursor.execute(
            'SELECT solution.id, solution.id_game, solution.difficulty, solution.col1, solution.col2, solution.col3, solution.col4, solution.col5, solution.col6, solution.col7, solution.col8,' +
            'solution.col9 FROM game, solution, users WHERE username = "' + username + 'AND user_id = users.id AND id_game = game.id;')

        # lista de tuple (id, id_game, difficulty, col1, col2 .. col9)
        all_data = cursor.fetchall()

        for e in all_data:
            id = e[0]

        for i in range(0, 9):
            cursor.execute('UPDATE game SET col' + str(i + 1) + ' = "' + m[i] + '" WHERE id = ' + str(id) + ';')

        self.db.commit()

    def abortGame(self, user):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = "' + user + '";')
        user_data = cursor.fetchall()

        cursor.execute('DELETE FROM solution WHERE user_id = ' + str(user_data[0][0]) + ';')
        cursor.execute('DELETE FROM game WHERE user_id = ' + str(user_data[0][0]) + ';')
        self.db.commit()

    # the board generating methods
    def findEmpty(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 0:
                    return y, x  # y = row , x = column
        # if we got here it means that we finished the sudoku, so return none
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
        # end condition:- getting to the end of the board - the function findEmpty returns NONE
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

    def generateLevel(self, difficulty, username):
        self.abortGame(username)
        self.generateRandomBoard(self.firstBoard)
        cursor = self.db.cursor()

        cursor.execute('SELECT * FROM users WHERE username = "' + username + '";')
        user_data = cursor.fetchall()

        if difficulty == "Easy":
            # update database, solution table
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES (1, "easy", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
            self.deleteCells(self.firstBoard, 30)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES ("easy", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
        elif difficulty == "Medium":
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES (1, "medium", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
            self.deleteCells(self.firstBoard, 35)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES ("medium", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
        else:
            # difficulty == "Hard" or invalid
            cursor.execute(
                'INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES (1, "hard", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
            self.deleteCells(self.firstBoard, 40)

            cursor.execute(
                'INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9, user_id)'
                ' VALUES ("hard", "' + ','.join([str(x) for x in self.firstBoard[:][0]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][1]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][2]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][3]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][4]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][5]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][6]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][7]]) + '", "' +
                ','.join([str(x) for x in self.firstBoard[:][8]]) + '", ' +
                str(user_data[0][0]) + ');')
            self.db.commit()
