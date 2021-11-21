import numpy as np


# def spiral_matrix(size):
#     for i in range(size):
#         for j in range(size):
#
#             # x stores the layer in which (i, j)'th element lies
#             # find minimum of four inputs
#             x = min(min(i, j), min(size - 1 - i, size - 1 - j))
#
#             # print upper right half
#             if i <= j:
#                 print(abs((size - 2 * x) * (size - 2 * x) - (i - x) - (j - x) - (size ** 2 + 1)), end='')
#
#             # print lower left half
#             else:
#                 print(abs((size - 2 * x - 2) * (size - 2 * x - 2) + (i - x) + (j - x) - (size ** 2 + 1)), end='')
#
#             print('\t', end='')
#         print()

def spiral_matrix(size):
    for i in range(size):
        for j in range(size):

            # x stores the layer in which (i, j)'th element lies
            # find minimum of four inputs
            x = min(min(i, j), min(size - 1 - i, size - 1 - j))

            # print upper right half
            if i <= j:
                print(abs((size - 2 * x) * (size - 2 * x) - (i - x) - (j - x) - (size ** 2 + 1)), end='')

            # print lower left half
            else:
                print(abs((size - 2 * x - 2) * (size - 2 * x - 2) + (i - x) + (j - x) - (size ** 2 + 1)), end='')

            print('\t', end='')
        print()


spiral_matrix(4)



spiral_matrix(1)
