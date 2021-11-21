import sqlite3


conn = sqlite3.connect('app.db')
cur = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS category (
	"category_id"	INTEGER,
	"category_name"	TEXT NOT NULL,
	PRIMARY KEY("category_id")
);
'''
cur.execute(sql)

sql = '''
INSERT INTO category (category_name) VALUES ('technology');
INSERT INTO category (category_name) VALUES ('e-commerce');
INSERT INTO category (category_name) VALUES ('gaming');
'''
cur.executescript(sql)

sql = '''
SELECT * FROM category;
'''
cur.execute(sql)
categories = cur.fetchall()
print(categories)


conn.commit()
conn.close()
