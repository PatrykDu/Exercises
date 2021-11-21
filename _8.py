def is_prime(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    if len(result) == 2:
        return True
    else:
        return False


print(is_prime(12))
