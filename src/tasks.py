import random
from discord.ext import tasks
from . import get_user_id, get_random_message_by_username


@tasks.loop(minutes=random.uniform(1, 15))
async def dm_random_message(client):
    user = await client.fetch_user(get_user_id('applause7'))
    print("User Acquired.")
    message = get_random_message_by_username('applause7')
    if user:
        await user.send(message)
        print("Message Sent.")
