import csv

# Configure so that the code is testable
def get_user_id(username, user_database='../data/users.csv'):
    with open(user_database, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return row['id']
    return None
