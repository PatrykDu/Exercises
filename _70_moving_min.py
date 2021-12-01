import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))

print(closes)


def moving_min(prices, window_size):
    minimums = []
    for m in range(len(prices) - window_size + 1):
        temp = []
        for i in range(window_size):
            temp.append(prices[m+i])
        minimum = min(temp)
        minimums.append(minimum)

    return minimums


print(moving_min(closes, 3))
