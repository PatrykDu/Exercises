def calculate():
    palindromes = []
    two_digits = []
    two_digits2 = []
    for i in range(10, 100):
        two_digits.append(i)
        two_digits2.append(i)

    result = []
    for x in two_digits:
        for y in two_digits2:
            result.append(x * y)
    print(result)
    for i in result:
        if str(i) == str(i)[::-1]:
            palindromes.append(i)
    return max(palindromes)


print(calculate())



