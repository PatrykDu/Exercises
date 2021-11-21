def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i != 0:
            i += 1
        else:
            number = number / i
            factors.append(i)
    else:
        if number != 1:
            factors.append(number)
    return factors


calculate(48)
