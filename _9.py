def is_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def calculate():
    primes = []
    number = 1
    while len(primes) < 100:
        if is_prime(number):
            primes.append(number)
            number += 1
        else:
            number += 1
    return primes[-1]


print(calculate())
