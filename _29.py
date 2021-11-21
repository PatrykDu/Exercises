import json


def json_to_csv():
    with open('users.json', 'r') as file:
        content = json.load(file)
    headers = ','.join(list(content[0].keys()))

    with open('users.csv', 'w') as file:
        file.write(headers + '\n')
        for user in content:
            x = list(user.values())
            output = ','.join([str(elem) for elem in x])
            file.write(output + '\n')


json_to_csv()
