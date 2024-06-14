import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from tasks import dm_random_message, send_scheduled_message

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)
botToken = os.getenv('BOT_TOKEN')


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')
    dm_random_message.start(client)
    send_scheduled_message.start(client)


@client.event
async def on_connect():
    print("Bot has connected to the server and is ready.")


client.run(os.environ['BOT_TOKEN'])
