from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NoticeboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join noticeboard group
        await self.channel_layer.group_add(
            "noticeboard_updates",  # Fixed group name to match signals
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave noticeboard group
        await self.channel_layer.group_discard(
            "noticeboard_updates",
            self.channel_name
        )

    async def send_update(self, event):
        """Receive message from room group and send to WebSocket"""
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event["content"]))