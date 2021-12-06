import csv


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(map(lambda row: (row[0], float(row[1]), float(row[4])), rows))


def find_doji(data):
    candles = {round(abs(item[1] - item[2]), 2): item[0] for item in data}
    x = min(candles.items(), key=lambda x: x[1])
    return candles[x[0]]


print(find_doji(data))
