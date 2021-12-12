x = [[3, 1, 6], [5, 2, 6], [5, 2, 6]]
y = [[4, 2, 7], [6, 3, 2], [1, 3, 5]]

# for row1, row2 in zip(x, y):
#     print(row1, row2)

z = zip(x, y)

# for i1, i2 in z:
#     for item1 in i1, i2:
#         print(item1)


print(x)
print('---------------------------------')
# for number in range(len(x[0])):
#     for row in x:
#         print(row[number])

output = [[row[number] for row in x] for number in range(len(x[0]))]

print('-----------------------------------')
print(output)
