from code import interact
from email import message
import discord
import random
from discord.utils import get

import json
import os  
src_file_path = os.path.dirname(__file__)

print(os.getcwd())
f = open(src_file_path + '/iBot.json')
data = json.load(f)
print(data)
print(type(data))
for detail in data['myBot']:
    print(detail) 
f.close()   

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have {0.user.name}'.format(client))

@client.event
async def on_connect():
    print('{0.user.name}'.format(client) + " just hop on!")
    for guilds in client.guilds:
        print('Guild:' + (str)(guilds))
        for channels in guilds.channels:
            if((str)(channels.name) == 'general'):
                await guilds.get_channel(channels.id).send('{0.user.name} is online!'.format(client))

@client.event
async def on_disconnect():
    print('{0.user}'.format(client) + " is shutting down")

@client.event
async def on_member_join(member):
    print(member.name + ' just slide through the server!')

@client.event
async def on_member_remove(member):
    print(member.name + ' just quit the server!')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('&hello'):
        await message.channel.send('Hello ' + message.author.mention + '!')
    if message.content.startswith('shutdown@'):
        print('ibot shutdown')
        await client.close()

token = (data["myBot"])[0]["token"]
print(token)
print(os.getcwd())
client.run(token)




