from django.shortcuts import render
from room.models import Room
# Create your views here.

def room(request):

        ob = Room.objects.all()
        context = {
            'value': ob
        }
        return render(request,"room/view_room.html")
