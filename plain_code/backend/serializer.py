from rest_framework import serializers
from .models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9']


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorMsg
        fields = ['msg']


class DiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyMsg
        fields = ['msg']
