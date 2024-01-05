"""
URL configuration for IS_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sudoku.views import ReactView, MsgView, DiffView, VictoryView, UserView, HintView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', ReactView.as_view(), name="sudoku"),
    path('errmsgs/', MsgView.as_view(), name="error messages"),
    path('diffmsgs/', DiffView.as_view(), name="difficulty messages"),
    path('victorymsgs/', VictoryView.as_view(), name="checking victory"),
    path('user/', UserView.as_view(), name="user data"),
    path('hint/', HintView.as_view(), name="hints")
]
