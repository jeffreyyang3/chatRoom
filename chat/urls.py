from django.conf.urls import url, include
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path("chat/<str:roomName>/", views.room),
    path("login", views.login)
]


