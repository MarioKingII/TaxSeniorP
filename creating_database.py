import sqlite3
conn = sqlite3.connect('tax_brackets.db')
cur = conn.cursor()

sql = '''
    CREATE TABLE taxbrackets (
    tax_rate FLOAT,
    single_start FLOAT,
    single_end FLOAT,
    married_start FLOAT,
    married_end FLOAT,
    primary key(tax_rate)
    )'''

cur.execute(sql)
conn.commit()
conn.close()

