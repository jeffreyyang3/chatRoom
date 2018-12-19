from django.conf.urls import url, include
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),

    # url(r'^$', views.index, name='index'),
	#url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path("chat/<str:roomName>/", views.room),
    path("login", views.login)
]


