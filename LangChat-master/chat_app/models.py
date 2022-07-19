from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    user1 = models.CharField(max_length=20, blank=True, null=True)
    user2 = models.CharField(max_length=20, blank=True, null=True)

class TempUser(models.Model):
    username = models.CharField(max_length=20)
    knows = models.CharField(max_length=20)
    learning = models.CharField(max_length=20)
    room_name = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, blank=True, null=True)

class OnlineUser(models.Model):
    username= models.CharField(max_length=20, blank=True, null=True)
    room_name = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='users')


