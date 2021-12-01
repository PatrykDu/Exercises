import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))

print(closes)


def moving_avg(prices, window_size):
    means = []
    for m in range(len(prices) - window_size + 1):
        temp = []
        for i in range(window_size):
            temp.append(prices[m+i])
        mean = sum(temp) / len(temp)
        means.append(round(mean, 2))

    return means


print(moving_avg(closes, 8))
