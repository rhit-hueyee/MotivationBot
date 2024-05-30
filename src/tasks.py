import random
from discord.ext import tasks
from utils import get_user_id


@tasks.loop(minutes=random.uniform(1, 15))
async def dm_random_message(client):
    user = await client.fetch_user(get_user_id('applause7'))
    print("User Acquired.")
    messages = ["Message"]
    if user:
        await user.send(random.choice(messages))
        print("Message Sent.")
