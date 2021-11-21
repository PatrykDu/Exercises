def calculate():
    numbers = []
    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(str(i))
    return str(len(numbers))



print(calculate())
