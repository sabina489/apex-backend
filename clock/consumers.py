import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now


class ClockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room
        self.room_group_name = "clock"

        # Join clock room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "check_clock",
                "message": "hello",
            },
        )

    async def disconnect(self, close_code):
        # Leave clock room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # message = "Hello my friend"

        # Send message to clock room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "check_clock",
                "message": message,
            },
        )

    # Receive message from clock room
    async def check_clock(self, event):
        message = event["message"]
        print(message)

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    # "message": "fellow"
                    "cur_time ": str(now())
                }
            )
        )

    async def get_exam(self, event):
        message = event["status"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({"status": message, "cur_time ": str(now())})
        )
