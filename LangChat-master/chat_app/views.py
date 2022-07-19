from django.shortcuts import render
from queue import Queue
from .models import TempUser, ChatRoom
from django.db.models.base import ObjectDoesNotExist

rus_speakers = Queue()
span_speakers = Queue()
eng_speakers = Queue()
germ_speakers = Queue()

# Create your views here.
def index(request):
    return render(request, "chat_app/index.html")

def chat(request):
    know_languages = request.POST["know-languages"]
    learning_languages = request.POST["learning-languages"]
    username = request.POST["username"]
    request.session["username"] = username
    try:
        match = TempUser.objects.filter(knows=learning_languages, learning=know_languages).first()
        print("found match")
        room_name = match.room_name.id
        match.delete()
    except (ObjectDoesNotExist, AttributeError) as e:
        print("caught exception")
        new_room = ChatRoom.objects.create()
        temp_user = TempUser.objects.create(username=username, knows=know_languages, learning=learning_languages, room_name=new_room)
        request.session["temp_user_id"] = temp_user.id
        request.session.modifed = True
        room_name = new_room.id
    return render(request, "chat_app/chat.html", {
        "know_lang": know_languages,
        "learning_lang": learning_languages,
        "room_name": room_name,
        "username": username,
    })