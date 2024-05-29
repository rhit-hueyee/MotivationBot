import discord
import asyncio
import random
from discord.ext import commands, tasks
import os
import csv
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)
botToken = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')
    dm_random_message.start() 

@client.event
async def on_connect():
    print("Bot has connected to the server and is ready.")

@tasks.loop(minutes=random.uniform(1, 15)) 
async def dm_random_message():
    user = await client.fetch_user(get_user_id('applause7')) 
    messages = ["Fat Fuck", "12% body fat","Fatass","No abs","150lbs", "Kill yourself", "Faggot", "Lazy Ass", "Not Twink"]
    if user:
        await user.send(random.choice(messages))

def get_user_id(username):
    with open('../data/users.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return row['id']
    return None

client.run(os.environ['BOT_TOKEN'])
 