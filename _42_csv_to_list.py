import csv

with open('Customer.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = tuple(reader)
    countries = []
    for row in rows:
        countries.append(row[8])

    unique_countries = set(countries)
    unique_countries = list(unique_countries)
    unique_countries.sort()

print(unique_countries)
