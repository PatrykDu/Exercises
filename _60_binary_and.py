def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]


def bitwise_and(x, y):

    if x < 0 or y < 0:
        raise ValueError('Both numbers must be positive')

    # to binary
    x = decimal_to_binary(x)
    y = decimal_to_binary(y)

    # set the same length
    length = max(len(x), len(y))

    if len(x) > len(y):
        t = len(x) - len(y)
        y = '0' * t + y
    elif len(y) > len(x):
        t = len(y) - len(x)
        x = '0' * t + x

    # calculate AND
    result = ''
    for num in range(len(x)):
        if x[num] == '1' and y[num] == '1':
            result += '1'
        else:
            result += '0'

    return int(result, 2)


print(bitwise_and(25, 19))
print(bitwise_and(-25, 19))
