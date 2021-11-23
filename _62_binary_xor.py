def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]


def bitwise_xor(x, y):

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

    # calculate OR
    result = ''
    for num in range(len(x)):
        if x[num] == '1' and y[num] == '0':
            result += '1'
        elif x[num] == '0' and y[num] == '1':
            result += '1'
            pass
        else:
            result += '0'

    return int(result, 2)


print(bitwise_xor(10, 140))
# print(bitwise_xor(-25, 19))
