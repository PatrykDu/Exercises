import json


def filter_active_users():
    with open('users.json', 'r') as file:
        content = json.load(file)
    output = []

    for user in content:
        if user['is_active']:
            output.append(user)

    with open('active_users.json', 'w') as file:
        json.dump(output, file, indent=2)


filter_active_users()
