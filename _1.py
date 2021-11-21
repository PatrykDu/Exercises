def calculate():
    numbers = []
    for i in range(100):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)
    all_numbers = sum(numbers)
    return all_numbers


print(calculate())
