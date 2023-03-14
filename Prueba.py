import csv
import sqlite3


def calculate_tax(taxable_income, filing_status):
    # Connect to the SQLite database
    conn = sqlite3.connect('tax_brackets.db')
    cursor = conn.cursor()

    # Retrieve the tax bracket for the given income and filing status
    if filing_status == 'single':
        cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= single_start AND ? <= single_end', (taxable_income, taxable_income))
        tax_bracket = cursor.fetchone()

    else:
        cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= married_start AND ? <= married_end', (taxable_income, taxable_income))
        tax_bracket = cursor.fetchone()

    # Calculate the tax amount based on the retrieved tax bracket and the taxable income
    tax_rate, _, _, _, _ = tax_bracket

    # Close the database connection and return the tax amount
    conn.close()
    return tax_rate

print(calculate_tax(100000, 'married'))