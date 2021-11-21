import sqlite3

conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id)
)''')

cur.execute('''INSERT INTO category (category_name) VALUES ('technology')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('e-commerce')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('gaming')''')


# Enter your solution here
sql = '''
UPDATE category 
SET category_name = 'online shop' 
WHERE category_id = 2
'''
cur.execute(sql)

sql = '''
SELECT * FROM category;
'''
cur.execute(sql)
categories = cur.fetchall()
for category in categories:
    print(category)


conn.close()
