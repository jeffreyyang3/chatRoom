from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import html


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, roomName):
    


    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(roomName)),
        'strippedName': mark_safe(json.dumps(roomName)).strip('\"') #take the quotes out of the room name json
        
    })

def login(request):
    return render(request, 'chat/login.html', {})