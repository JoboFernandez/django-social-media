from django.contrib.auth.models import User
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from ..models import Thread, Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        logged_user = self.scope['user']
        other_user = User.objects.get(username=self.scope['url_route']['kwargs']['username'])
        self.thread_obj = Thread.objects.get_or_create_personal_thread(logged_user, other_user)

        self.room_group_name = f'personal_thread_{self.thread_obj.id}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        Message.objects.create(thread=self.thread_obj, sender=self.scope['user'], text=text_data_json['message'])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': self.scope['user'].username,
                'message': text_data_json['message'],
            }
        )

    def chat_message(self, event):
        self.send(json.dumps({
            'type': 'chat',
            'sender': event['sender'],
            'message': event['message'],
        }))

    def disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

