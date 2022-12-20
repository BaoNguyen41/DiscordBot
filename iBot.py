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
    print('hello world')
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
        print(guilds)
        for channels in guilds.channels:
            print('Name: ' + channels.name) 


async def on_disconnect():
    print('{0.user}'.format(client) + " is shutting down")

@client.event
async def on_member_join(member):
    print(member.name + ' just slide through the server!')
async def on_member_remove(member):
    print(member.name + ' just quit the server!')
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    for message in client.guilds:
        await message.channel.send('^')
    if message.content.startswith('&hello'):
        await message.channel.send('Hello ' + message.author.mention + '!')
#data is a dict, data["myBot"] give a list of dict, (data["myBot"])[0] give the dict "token", (data["myBot"])[0]["token"] get the value of token
token = (data["myBot"])[0]["token"]
print(token)
print(os.getcwd())
client.run(token)




