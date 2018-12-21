from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from urllib.parse import quote


class ChatConsumer(AsyncWebsocketConsumer):
		async def connect(self):
				self.room_name = self.scope['url_route']['kwargs']['room_name']

				self.room_group_name = 'chat_%s' % self.room_name

				
				await self.channel_layer.group_add(
						self.room_group_name,
						self.channel_name
				)

				await self.accept()


		async def disconnect(self, close_code):
				
				await self.channel_layer.group_discard(
						self.room_group_name,
						self.channel_name
				)

		async def receive(self, text_data):
				text_data_json = json.loads(text_data)
				message = text_data_json['message']
				username = text_data_json['username']
				userID = text_data_json['userID']
		
				isAnonymous = text_data_json['isAnonymous']
				isInstructor = text_data_json['isInstructor']
				invisible = text_data_json['invisible']

				if isInstructor:
					text_data_json['instructorChannel'] = self.channel_name
				

				
				# Send message to room group
				instructorChannel = text_data_json.get("instructorChannel")
				if(instructorChannel and instructorChannel != "notIt"):
					await self.channel_layer.send(text_data_json.get("instructorChannel"), {
						'type': 'chat_message',
						'message': message,
						'username': username,
						'isAnonymous': isAnonymous,
						'isInstructor': isInstructor,
						'userID': userID,
						'instructorChannel': text_data_json['instructorChannel'],
						'forInstructor': True,
						'invisible': invisible,
					})

				if(isAnonymous):
					username = "Anonymous"
				
				await self.channel_layer.group_send(
						self.room_group_name,{
							'type': 'chat_message',
							'message': message,
							'username': username,
							'isAnonymous': isAnonymous,
							'isInstructor': isInstructor,
							'userID': userID,
							'instructorChannel': text_data_json.get("instructorChannel"),
							'forInstructor': False,
							'invisible': invisible
						})
				

				
		async def chat_message(self, event):
				message = event['message']
				username = event['username']
				isAnonymous = event['isAnonymous']
				instructorChannel = event['instructorChannel']
				userID = event['userID']
				forInstructor = event['forInstructor']
				invisible = event['invisible']

				await self.send(text_data=json.dumps({
						'message': message,
						'username': username,
						'isAnonymous': isAnonymous,
						'instructorChannel': instructorChannel,
						'userID': userID,
						'forInstructor': forInstructor,
						'invisible': invisible,
				}))

