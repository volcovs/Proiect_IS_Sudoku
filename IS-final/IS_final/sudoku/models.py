from django.db import models


class React(models.Model):
    col1 = models.CharField(max_length=18)
    col2 = models.CharField(max_length=18)
    col3 = models.CharField(max_length=18)
    col4 = models.CharField(max_length=18)
    col5 = models.CharField(max_length=18)
    col6 = models.CharField(max_length=18)
    col7 = models.CharField(max_length=18)
    col8 = models.CharField(max_length=18)
    col9 = models.CharField(max_length=18)


class ErrorMsg(models.Model):
    msg = models.CharField(max_length=100)


class DifficultyMsg(models.Model):
    msg = models.CharField(max_length=7)


class VictoryMsg(models.Model):
    msg = models.CharField(max_length=7)


class UserMsg(models.Model):
    type = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    games_won = models.IntegerField()
    games_total = models.IntegerField()
    time_total = models.CharField(max_length=8)
    best_time = models.CharField(max_length=8)


class Hint(models.Model):
    hint = models.IntegerField()
    xhint = models.IntegerField()
    yhint = models.IntegerField()
