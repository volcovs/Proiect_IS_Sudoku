from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8', 'row9']
