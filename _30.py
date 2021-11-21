from collections import namedtuple
import json


def json_to_object():
    # Extract data
    with open('users.json', 'r') as file:
        content = json.load(file)

    # Extract all names
    headers = tuple(content[0].keys())

    # Create a User class
    User = namedtuple('User', headers)

    # Create and return instances of the user class
    output = []
    for data in content:
        user = tuple(data.values())
        output.append(User(*user))

    return output


print(json_to_object())
