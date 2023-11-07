import mysql.connector

class Model():
    def __init__(self, host, user, password, db_name):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=3306,
            database=db_name
        )


    def databaseToMatrix(self, table_name):
        m = []

        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM ' + table_name +' LIMIT 1')

        # lista de tuple (id, difficulty, row1, row2 .. row9)
        all_data = cursor.fetchall()

        for e in all_data:
            for i in range(2, 11):
                m.append([int(c) for c in e[i]])

        return m


    def checkCorrect(self, m, solution, num, i, j):
        # functia primeste matricea de joc, cifra noua si pozitia pe care a fost adaugata cifra

        # deja cifra in acel patrat
        flagValid = m[i][j] == 0

        # verificare rand i
        flagRow = len([e for e in m[i] if e == num]) == 0

        # verificare rand j
        flagColumn = len([e[j] for e in m if e[j] == num]) == 0

        # verificare patrat 3x3
        squareRow1 = m[i/3][:3]
        squareRow2 = m[i/3+1][0:3]
        squareRow3 = m[i/3+2][:3]

        flagSquare = not (num in squareRow1 or num in squareRow2 or num in squareRow3)

        # if the solution is known
        return num == solution[i][j] and flagValid

        # return flagValid and flagRow and flagColumn and flagSquare


    def addNumber(self, m, solution, num, i, j):
        if self.checkCorrect(m, solution, num, i, j):
            m[i][j] = num
            for r in m:
                if len([e for e in r if e == 0]) == 0:
                    print("You won")
        else:
            print("Incorrect number")
            # maybe show the number with red on the website
            # perhaps return different int values for each error