from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *


class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"row1": output.row1, "row2": output.row2, "row3": output.row3, "row4": output.row4, "row5": output.row5,
                   "row6": output.row6, "row7": output.row7, "row8": output.row8, "row9": output.row9}
                for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)