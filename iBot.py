from code import interact
from email import message
import discord
import random
from discord.utils import get

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
            print('Name: ' + channels.name) #841780253038346291


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
    if message.content.startswith('&hello'):
        #emoji = get(client.get_emojis(), name = ':smiling_imp:')
        emojis = ':smiling_imp'
        #await client.add_reaction(emojis)
        await message.channel.send('Hello ' + message.author.mention + '!')
client.run(token)



