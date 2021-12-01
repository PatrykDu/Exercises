# import pandas as pd
#
#
# def moving_avg():
#     df = pd.read_csv('cdr.csv')
#     close = []
#     for c in df['Close']:
#         close.append(c)
#     means = []
#     for m in range(len(close) - 2):
#         mean = (close[m] + close[m + 1] + close[m + 2]) / 3
#         means.append(round(mean, 2))
#
#     return means


def moving_avg():

    close = []
    with open('cdr.csv') as cdr:
        next(cdr)
        for r in cdr:
            row = r.split(',')
            close.append(float(row[4]))
        means = []
        for m in range(len(close) - 2):
            mean = (close[m] + close[m + 1] + close[m + 2]) / 3
            means.append(round(mean, 2))

        return means


print(moving_avg())
