from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


def decompress(number):
    number = number.split('_')
    output = ''
    for item in number:
        output += str(item[0] * int(item[1]))
    return int(output)


print(decompress('14_53_22_51_02'))
print(decompress('11_03_51_03'))
