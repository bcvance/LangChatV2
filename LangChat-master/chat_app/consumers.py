import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import TempUser
from django.db.models.base import ObjectDoesNotExist
import threading

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'connected!'
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
        

    async def disconnect(self, close_code):
        self.thread = threading.Thread(target=self.delete_users)
        self.thread.start()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        del self.thread

    def delete_users(self):
        if TempUser.objects.get(id = self.scope["session"]["temp_user_id"]):
            TempUser.objects.get(id = self.scope["session"]["temp_user_id"]).delete()
