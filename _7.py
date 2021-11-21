def greatest_common_divisor(number1, number2):
    bigger_numbers = max(number1, number2)
    while True:
        if number1 % bigger_numbers == 0 and number2 % bigger_numbers ==0:
            return bigger_numbers
        else:
            bigger_numbers -= 1


print(greatest_common_divisor(32, 48))
