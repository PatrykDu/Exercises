def calculate():
    fibonacci = [0, 1]
    i = 2
    while fibonacci[-1] < 1000000:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1
    sum_of_even = 0
    for x in fibonacci:
        if x % 2 == 0:
            sum_of_even = sum_of_even + x
    return sum_of_even


print(calculate())
