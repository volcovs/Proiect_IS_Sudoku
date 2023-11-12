import mysql.connector

class Model_Sudoku():
    def __init__(self, host, user, password, db_name):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=3306,
            database=db_name
        )


    def newGame(self):
        m = []

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM game LIMIT 1')

        # lista de tuple (id, difficulty, row1, row2 .. row9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(2, 11):
                m.append(e[i])

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

        return m


    def checkCorrectIneff(self, m, solution):
        matrix1 = [e.split(",") for e in m]
        matrix2 = [e.split(",") for e in solution]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] != '0' and matrix1[i][j] != matrix2[i][j]:
                    return False, i, j

        return True, 0, 0

    def checkCorrect(self, m, solution, num, i, j):
        # functia primeste matricea de joc, cifra noua si pozitia pe care a fost adaugata cifra

        # deja cifra in acel patrat
        flagValid = m[i][j] == 0

        # verificare rand i
        flagRow = len([e for e in m[i] if e == num]) == 0

        # verificare rand j
        flagColumn = len([e[j] for e in m if e[j] == num]) == 0

        # verificare patrat 3x3
        squareRow1 = m[i//3][:3]
        squareRow2 = m[i//3+1][0:3]
        squareRow3 = m[i//3+2][:3]

        flagSquare = not (num in squareRow1 or num in squareRow2 or num in squareRow3)

        # if the solution is known
        return num == solution[i][j] and flagValid

        # return flagValid and flagRow and flagColumn and flagSquare


    def addNumber(self, m, solution, num, i, j):
        if self.checkCorrect(m, solution, num, i, j):
            m[i][j] = num

            #constructor for the updated row on the sudoku board
            row = ""
            for e in m[i]:
                row = row + str(e)

            #get the id of the game to be updated
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM solution LIMIT 1')

            # lista de tuple (id, difficulty, row1, row2 .. row9)
            all_data = cursor.fetchall()

            for e in all_data:
                id = e[0]

            #update database
            cursor = self.db.cursor()
            cursor.execute('UPDATE game SET row' + str(i+1) + ' = "' + row + '" WHERE id = ' + str(id))
            self.db.commit()

            for r in m:
                if len([e for e in r if e == 0]) == 0:
                    print("You won")
        else:
            print("Incorrect number")
            # maybe show the number with red on the website
            # perhaps return different int values for each error


    def abortGame(self):
        cursor = self.db.cursor()
        cursor.execute('DELETE * FROM solution LIMIT 1')
        cursor.execute('DELETE * FROM game LIMIT 1')
        self.db.commit()