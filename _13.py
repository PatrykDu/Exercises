from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    output = '_'.join(result)
    return output


print(compress(100000))
