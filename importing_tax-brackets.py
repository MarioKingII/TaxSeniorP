import sqlite3
import csv
import chardet

connection = sqlite3.connect('tax_brackets.db')
cursor = connection.cursor()


with open('taxbracket.csv', 'r') as file: 
    reader = csv.reader(file)
    next(reader)
    no_records = 0 
    for row in file:
        cursor.execute('INSERT INTO taxbrackets VALUES (?,?,?,?,?)', row.split(','))
        connection.commit()
        no_records += 1 

connection.close()
