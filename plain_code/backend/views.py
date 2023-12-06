from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from . import model

m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
aux = m.newGame()
board = m.newGame()
solutionToGame = m.newGameSolution()

class ReactView(APIView):
    serializer_class = ReactSerializer

    # always sends the board saved inside the database
    def get(self, request):
        # m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
        # board = m.newGame()

        # resp = [{"row1": output.row1, "row2": output.row2, "row3": output.row3, "row4": output.row4, "row5": output.row5,
        # "row6": output.row6, "row7": output.row7, "row8": output.row8, "row9": output.row9}
        # for output in React.objects.all()]

        resp = [{"col1": board[0], "col2": board[1], "col3": board[2], "col4": board[3], "col5": board[4],
                 "col6": board[5], "col7": board[6], "col8": board[7], "col9": board[8]}]

        return Response(resp)

    # receives the new board configuration, checks it and if a number from the solution has been found
    # , updates the database
    def post(self, request):
        React.objects.all().delete()

        # m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
        # solutionToGame = m.newGameSolution()

        serializer = ReactSerializer(data=request.data)
        # aux = m.newGame()

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
                # m.updateDatabase(board)
                pass

            serializer.save()
            return Response(serializer.data)


class MsgView(APIView):
    serializer_class = MsgSerializer

    # checks the current board and returns an error message if something is wrong
    def get(self, request):
        # m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
        # board = m.newGame()
        # solutionToGame = m.newGameSolution()

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
        # m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
        DifficultyMsg.objects.all().delete()

        serializer = DiffSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data['msg'] == "Easy":
                # render easy level of sudoku
                print('easy game')
                m.generateLevel("Easy")
            elif serializer.validated_data['msg'] == "Medium":
                # render medium level of sudoku
                print('medium game')
                m.generateLevel("Medium")
            elif serializer.validated_data['msg'] == "Hard":
                # render hard level of sudoku
                print('hard game')
                m.generateLevel("Hard")
            else:
                print('Invalid difficulty choice')

            serializer.save()
            return Response(serializer.data)
