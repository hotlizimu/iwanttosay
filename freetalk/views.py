from django.shortcuts import render, redirect, get_object_or_404
from .models import Rooms
from .forms import JoinRoom, WriteMessage


def start(request):
    if request.method != 'POST':
        form = JoinRoom()
    else:
        form = JoinRoom(data=request.POST)
        if form.is_valid():
            getform = form.save(commit=False)
            if Rooms.objects.filter(number=getform.number).exists():
                return redirect('freetalk:room', number=getform.number)
            else:
                form.save()
                return redirect('freetalk:room', number=getform.number)
    return render(request, 'start.html', {'form': form})


def room(request, number):
    this_room = get_object_or_404(Rooms, number=number)
    messages = this_room.messages_set.order_by('-date_added')
    if request.method != 'POST':
        form = WriteMessage()
    else:
        form = WriteMessage(data=request.POST)
        if form.is_valid():
            getform = form.save(commit=False)
            getform.room = this_room
            getform.save()
            return redirect("freetalk:room", number=number)
    return render(request, 'room.html', {'room': this_room, 'form': form, 'messages': messages})
