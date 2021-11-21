def binary_to_int():
    file = open('binary.txt', 'r').read()
    output = []
    file = file.split()
    for number in file:
        output.append(int(number, 2))
    return output


print(binary_to_int())
