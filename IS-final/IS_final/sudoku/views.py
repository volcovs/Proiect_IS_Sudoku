from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from . import model


class ReactView(APIView):
    m = model.Model_Sudoku('localhost', 'root', 'TheHateUGive13$', 'sudoku')
    board = m.newGame()
    solutionToGame = m.newGameSolution()

    serializer_class = ReactSerializer

    def get(self, request):
        #resp = [{"row1": output.row1, "row2": output.row2, "row3": output.row3, "row4": output.row4, "row5": output.row5,
                  # "row6": output.row6, "row7": output.row7, "row8": output.row8, "row9": output.row9}
               # for output in React.objects.all()]

        resp = [{"row1": self.board[0], "row2": self.board[1], "row3": self.board[2], "row4": self.board[3], "row5": self.board[4],
             "row6": self.board[5], "row7": self.board[6], "row8": self.board[7], "row9": self.board[8]}]

        return Response(resp)

    def post(self, request):
        React.objects.all().delete()

        serializer = ReactSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.board[0] = serializer.validated_data['row1']
            self.board[1] = serializer.validated_data['row2']
            self.board[2] = serializer.validated_data['row3']
            self.board[3] = serializer.validated_data['row4']
            self.board[4] = serializer.validated_data['row5']
            self.board[5] = serializer.validated_data['row6']
            self.board[6] = serializer.validated_data['row7']
            self.board[7] = serializer.validated_data['row8']
            self.board[8] = serializer.validated_data['row9']

            flag, x, y = self.m.checkCorrectIneff(self.board, self.solutionToGame)
            if not flag:
                print(f'Incorrect number on row {x+1}, column {y+1}!')
            else:
                print("Correct so far")

            serializer.save()
            return Response(serializer.data)