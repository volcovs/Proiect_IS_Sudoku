from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from . import model
import time

m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
board = []
solutionToGame = []
# by default, the user will be anonymous until they log in
user = "anon"

class ReactView(APIView):
    serializer_class = ReactSerializer

    # always sends the board saved inside the database
    def get(self, request):
        global board
        global solutionToGame
        global user

        # necessary delay, otherwise the sql connection can't handle the requests
        time.sleep(0.1)
        board = m.newGame(user)
        solutionToGame = m.newGameSolution(user)

        resp = [{"col1": board[0], "col2": board[1], "col3": board[2], "col4": board[3], "col5": board[4],
                "col6": board[5], "col7": board[6], "col8": board[7], "col9": board[8]}]

        return Response(resp)

    # receives the new board configuration, checks it and if a number from the solution has been found
    # , updates the database
    def post(self, request):
        React.objects.all().delete()
        global board
        global solutionToGame
        global user

        serializer = ReactSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            board[0] = serializer.validated_data['col1']
            board[1] = serializer.validated_data['col2']
            board[2] = serializer.validated_data['col3']
            board[3] = serializer.validated_data['col4']
            board[4] = serializer.validated_data['col5']
            board[5] = serializer.validated_data['col6']
            board[6] = serializer.validated_data['col7']
            board[7] = serializer.validated_data['col8']
            board[8] = serializer.validated_data['col9']

            flag, x, y = m.checkCorrectIneff(board, solutionToGame)
            if flag:
                m.updateDatabase(board, user)

            serializer.save()
            return Response(serializer.data)


class MsgView(APIView):
    serializer_class = MsgSerializer

    # checks the current board and returns an error message if something is wrong
    def get(self, request):
        global board
        global solutionToGame
        string = "Correct so far"

        flag, x, y = m.checkCorrectIneff(board, solutionToGame)
        if not flag:
            string = f'Incorrect number on row {y + 1}, column {x + 1}!'

        resp = [{"msg": string}]

        return Response(resp)

    # not really any need for POST requests
    def post(self, request):
        ErrorMsg.objects.all().delete()

        serializer = MsgSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class DiffView(APIView):
    serializer_class = DiffSerializer

    # there isn't really any need for GET requests
    def get(self, request):
        resp = [{"msg": " "}]

        return Response(resp)

    # checks the message received from client, and generates a new board of specified difficulty
    def post(self, request):
        global board
        global solutionToGame
        global user

        DifficultyMsg.objects.all().delete()
        serializer = DiffSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data['msg'] == "Easy":
                # render easy level of sudoku
                print('easy game')
                m.generateLevel("Easy", user)
            elif serializer.validated_data['msg'] == "Medium":
                # render medium level of sudoku
                print('medium game')
                m.generateLevel("Medium", user)
            elif serializer.validated_data['msg'] == "Hard":
                # render hard level of sudoku
                print('hard game')
                m.generateLevel("Hard", user)
            else:
                # continue game or invalid choice
                print('Continue game or invalid difficulty choice')

            board = m.newGame(user)
            solutionToGame = m.newGameSolution(user)

            serializer.save()
            return Response(serializer.data)


class VictoryView(APIView):
    serializer_class = VictorySerializer

    def get(self, request):
        global board
        global solutionToGame
        string = "False"

        flag = m.checkVictory(board, solutionToGame)
        if flag:
            string = "Victory"

        resp = [{"msg": string}]

        return Response(resp)

    # no need for post requests
    def post(self, request):
        VictoryMsg.objects.all().delete()

        serializer = VictorySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        # returns data to be displayed on the user's personal page
        global board
        global solutionToGame
        global user

        user_data = m.getAllUserData(user)
        resp = [{"type": "get", "username": user_data[0][1], "password": user_data[0][4], "first_name": user_data[0][2], "last_name": user_data[0][3],
                 "games_won": user_data[0][5], "games_total": user_data[0][6], "time_total": user_data[0][7],
                 "best_time": user_data[0][8]}]

        return Response(resp)

    def post(self, request):
        # receives the data from either 'create account' or 'log in'
        global board
        global solutionToGame
        global user

        UserMsg.objects.all().delete()
        serializer = UserSerializer(data=request.data)

        # receive user data from React
        if serializer.is_valid(raise_exception=True):
            request_type = serializer.validated_data['type']
            if request_type == "create":
                m.addNewUserToDatabase(serializer.validated_data)
                user = serializer.validated_data['username']
            elif request_type == "login":
                user = m.getUserFromDatabase(serializer.validated_data['username'], serializer.validated_data['password'])
                # load the game corresponding to the current user
                board = m.newGame(user)
                solutionToGame = m.newGameSolution(user)

            serializer.save()
            return Response(serializer.data)


class HintView(APIView):
    serializer_class = HintSerializer

    def get(self, request):
        global board
        global solutionToGame

        hint = m.getHint(board, solutionToGame)
        resp = [{"hint": int(hint[0]), "xhint": hint[1], "yhint": hint[2]}]

        return Response(resp)

    def post(self, request):
        Hint.objects.all().delete()

        serializer = HintSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
