from itertools import groupby


def compress(number):
    result = []
    temp = []
    output = ''
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    for item in result:
        temp.append(item[0] + int(item[1]) * '.')
    for ele in temp:
        output += ele
    return output


print(compress(111155522500))
