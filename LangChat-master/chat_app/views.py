from django.shortcuts import render
from queue import Queue
from .models import OnlineUser, TempUser, ChatRoom
from django.db.models.base import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers


rus_speakers = Queue()
span_speakers = Queue()
eng_speakers = Queue()
germ_speakers = Queue()

# Create your views here.
def index(request):
    num_online = OnlineUser.objects.all().count()
    return render(request, "chat_app/index.html", context={
        "num_online": num_online,
    })

def chat(request):
    know_languages = request.POST["know-languages"]
    learning_languages = request.POST["learning-languages"]
    username = request.POST["username"]
    request.session["username"] = username
    try:
        match = TempUser.objects.filter(knows=learning_languages, learning=know_languages).first()
        print("found match")
        room_name = match.room_name.id
        room = match.room_name
        online_user = OnlineUser.objects.create(username=username, room_name=room)
        room.user2 = online_user.username
        room.save()
        request.session['online_user_id'] = online_user.id
        request.session.modified = True
        match.delete()
    except (ObjectDoesNotExist, AttributeError) as e:
        print("caught exception")
        new_room = ChatRoom.objects.create()
        online_user = OnlineUser.objects.create(username=username, room_name=new_room)
        temp_user = TempUser.objects.create(username=username, knows=know_languages, learning=learning_languages, room_name=new_room)
        new_room.user1 = online_user.username
        new_room.save()
        request.session["temp_user_id"] = temp_user.id
        request.session['online_user_id'] = online_user.id
        request.session.modifed = True
        room_name = new_room.id
    return render(request, "chat_app/chat.html", {
        "know_lang": know_languages,
        "learning_lang": learning_languages,
        "room_name": room_name,
        "username": username,
    })

# @api_view(['GET'])
# def get_users(request, room_name):
#     data = serializers.serialize('json', ChatRoom.objects.filter(id = room_name), fields=['user1', 'user2'])
#     print(data)
#     room = ChatRoom.objects.get(id=room_name)
#     return Response(data)