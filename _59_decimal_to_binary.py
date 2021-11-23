def decimal_to_binary(digit):
    result = ''
    if digit == 0:
        return '0'
    else:
        while digit > 0:
            result = result + str(digit % 2)
            digit = int(digit/2)
        return result[::-1]


print(decimal_to_binary(81))
