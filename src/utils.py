import csv
import random


# Configure so that the code is testable
def get_user_id(username, user_database='../data/users.csv'):
    with open(user_database, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return row['id']
    return None


# Need exception handling for this function
def get_random_message_by_username(username,
                                   message_db='../data/messages.csv'):
    messages = []

    with open(message_db, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                messages.append(row[1])
                # Add message to list if username matches

    # Randomly select a message from the list
    if messages:
        return random.choice(messages)
    else:
        return "No messages found for this user."
