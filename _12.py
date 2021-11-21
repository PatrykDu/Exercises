from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    return result


print(compress(111155522500))
print('------------------------------------------')
print(compress(1000040000))
print('------------------------------------------')
print(compress(222775477284))
