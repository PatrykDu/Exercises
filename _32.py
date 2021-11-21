import sqlite3


# Create connection here
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# Create table
sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)

# Add record
sqlite_insert_query = """INSERT INTO customer
                          (first_name, last_name, email) 
                          VALUES ('John', 'Smith', 'john.smith@esmartdata.org');"""
cur.execute(sqlite_insert_query)

conn.commit()
conn.close()

