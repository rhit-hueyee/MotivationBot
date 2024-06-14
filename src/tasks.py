import random
from discord.ext import tasks
import datetime
from . import get_user_id, get_random_message_by_username, get_user_message_by_time  # noqa: E501


@tasks.loop(minutes=random.uniform(1, 15))
async def dm_random_message(client):
    user = await client.fetch_user(get_user_id('applause7'))
    print("User Acquired.")
    message = get_random_message_by_username('applause7')
    if user:
        await user.send(message)
        print("Message Sent.")


@tasks.loop(minutes=1)  # Checks every minute if it's time to send the message
async def send_scheduled_message(client):
    # Get the current time in the required format
    now = datetime.datetime.now().strftime("%H:%M")
    # Retrieve the scheduled message for 'applause7' at the current time
    message = get_user_message_by_time('applause7', now)
    if message:
        user = await client.fetch_user(get_user_id('applause7'))
        if user:
            await user.send(message)
            print(f"Scheduled message sent: {message}")
        else:
            print("User not found.")
    else:
        print("No scheduled message to send at this time.")
