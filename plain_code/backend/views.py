from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from . import model
import time

m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
board = []
solutionToGame = []

class ReactView(APIView):
    serializer_class = ReactSerializer

    # always sends the board saved inside the database
    def get(self, request):
        global board
        global solutionToGame

        # necessary delay, otherwise the sql connection can't handle the requests
        time.sleep(0.1)
        board = m.newGame()
        solutionToGame = m.newGameSolution()

        resp = [{"col1": board[0], "col2": board[1], "col3": board[2], "col4": board[3], "col5": board[4],
                "col6": board[5], "col7": board[6], "col8": board[7], "col9": board[8]}]

        return Response(resp)

    # receives the new board configuration, checks it and if a number from the solution has been found
    # , updates the database
    def post(self, request):
        React.objects.all().delete()
        global board
        global solutionToGame

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
                m.updateDatabase(board)

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
                # continue game or invalid choice
                print('Continue game or invalid difficulty choice')

            board = m.newGame()
            solutionToGame = m.newGameSolution()

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
