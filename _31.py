from collections import namedtuple
import json, pickle


with open('users.json', 'r') as file:
    content = json.load(file)

headers = tuple(content[0].keys())
User = namedtuple('User', headers)
values = [tuple(user.values()) for user in content]
users = [User(*user) for user in values]

pickle.dump(users, open('users.pickle', 'wb'))
content = pickle.load(open('users.pickle', 'rb'))
print(content[3])
