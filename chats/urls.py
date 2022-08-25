from django.urls import path

from . import views


app_name = 'chats'
urlpatterns = [
    path('', views.lobby, name="lobby"),
    path('<str:username>/', views.personal, name="personal"),
]

