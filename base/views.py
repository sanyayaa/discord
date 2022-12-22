from django.shortcuts import render,redirect 
from .models import Room,Topic
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'lets learn python'},
#     {'id':2, 'name': 'Design with me'},
#     {'id':3, 'name': 'Frontend developers'},
# ]

def index(request):
    q=request.GET.get('q')
    rooms = Room.objects.filter(topic__name=q) 
    topics = Topic.objects.all()

    context = {'rooms' : rooms, 'topics':topics}
    return render(request, 'base/index.html' , context )
 
def room( request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id = pk)
    context = { 'room' : room }
    return render(request, 'base/room.html',context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}

    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'form':form}

    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.method =='POST':
        room.delete()
        return redirect('index')

    return render(request,'base/delete.html',{'obj':room})