from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    pass

class TempUser(models.Model):
    username = models.CharField(max_length=20)
    knows = models.CharField(max_length=20)
    learning = models.CharField(max_length=20)
    room_name = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="users", blank=True, null=True)


