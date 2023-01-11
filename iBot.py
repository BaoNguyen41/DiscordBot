import discord
import random
import asyncio
from discord.utils import get

import json
import os  
src_file_path = os.path.dirname(__file__)

f = open(src_file_path + '/iBot.json')
data = json.load(f)
f.close()   

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

"""@client.event
async def on_ready():
    print('We have {0.user.name}'.format(client))"""

@client.event
async def on_connect():
    for guilds in client.guilds:
        for channels in guilds.channels:
            if((str)(channels.name) == 'bot-command'):
                await guilds.get_channel(channels.id).send('{0.user.name} is online!'.format(client))

@client.event
async def on_disconnect():
    print('{0.user.name}'.format(client) + " is shutting down")

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
    if message.content == "&hello":
        await message.add_reaction("👋")
        await message.reply('Hello ' + message.author.mention + '!', reference = message)
    if message.content.startswith('shutdown@'):
        await message.add_reaction("😴")
        await client.close()

token = (data["myBot"])[0]["token"]
print(token)
print(os.getcwd())
client.run(token)