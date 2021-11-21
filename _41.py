import csv
import sqlite3


product_constraints = [
    'INTEGER PRIMARY KEY',
    'TEXT NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'TEXT NOT NULL',
    'REAL NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL'
]


def generate_sql(table_name, col_names, constraints):
    cols = [" ".join((col, constraint)).strip()
            for col, constraint in zip(col_names, constraints)]
    return f'CREATE TABLE IF NOT EXISTS {table_name} (' + ', '.join(cols) + ')'


# Enter your solution here
# Connection
conn = sqlite3.connect('store.db')
cur = conn.cursor()

# Create Table
data = []
with open('Product.csv', 'r', encoding='UTF-8') as file:
    for line in file:
        data.append(line.strip())
columns = data.pop(0).split(',')

sql = generate_sql('Product', columns, product_constraints)
cur.execute(sql)

# INSERT DATA
insert_data_query = ''
for item in data:
    item = tuple(item.replace('"', '').split(','))
    query = '''
    INSERT OR IGNORE INTO Product
    VALUES {};
    '''.format(item)
    cur.execute(query)

# Read all data from Product
query = '''
SELECT COUNT(*) FROM Product
'''
cur.execute(query)
result = cur.fetchall()
print(result[0][0])

# Commit and close
conn.commit()
conn.close()
