from django.db import models
import sqlite3

class TaxCalculation(models.Model):
    gross_income = models.FloatField()
    federal_tax = models.FloatField()
    standard_deduction = 12200
    filling_status = models.SmallIntegerField()
    tax_bracket = models.DecimalField(max_digits=4, decimal_places=2)
    single_start = models.DecimalField(max_digits=10, decimal_places=2)
    single_end = models.DecimalField(max_digits=10, decimal_places=2)
    married_start = models.DecimalField(max_digits=10, decimal_places=2)
    married_end = models.DecimalField(max_digits=10, decimal_places=2)
    charitable_contributions = models.FloatField()
    college_expenses = models.FloatField()
    student_loan_interest = models.FloatField()
    taxes_registration = models.FloatField()
    interest_taxes = models.FloatField()
    medical_expenses = models.FloatField()
    retirement_contributions = models.FloatField()
    scholarships_received = models.FloatField()
 

    def calculate_standard_tax(self):
        
        taxable_income_stand = (self.gross_income - self.standard_deduction) + self.scholarships_received - self.retirement_contributions
        
        conn = sqlite3.connect('tax_brackets.db')
        cursor = conn.cursor()

        # Retrieve the tax bracket for the given income and filing status
        if self.filling_status == 'Single':
            cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= single_start AND ? <= single_end', (taxable_income_stand, taxable_income_stand))
            tax_bracket = cursor.fetchone()

        else:
            cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= married_start AND ? <= married_end', (taxable_income_stand, taxable_income_stand))
            tax_bracket = cursor.fetchone()

        # Calculate the tax amount based on the retrieved tax bracket and the taxable income
        tax_rate, _, _, _, _ = tax_bracket

        # Close the database connection and return the tax amount
        conn.close()
        
        to_view =[]
        return_Stand = (taxable_income_stand * tax_rate) - self.federal_tax
        to_view.append(tax_rate)
        to_view.append(return_Stand)
        to_view.append(taxable_income_stand)

        return to_view

    def calculate_itemized_tax(self):

        deductible_medical_expenses = self.gross_income * 0.075
        if self.medical_expenses < deductible_medical_expenses:
            self.medical_expenses = 0

        taxable_income_itemized = self.gross_income - self.charitable_contributions - self.college_expenses - self.student_loan_interest + self.scholarships_received - self.taxes_registration - self.interest_taxes - self.medical_expenses - self.retirement_contributions

        conn = sqlite3.connect('tax_brackets.db')
        cursor = conn.cursor()

        # Retrieve the tax bracket for the given income and filing status
        if self.filling_status == 'Single':
            cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= single_start AND ? <= single_end', (taxable_income_itemized, taxable_income_itemized))
            tax_bracket = cursor.fetchone()

        else:
            cursor.execute(f'SELECT * FROM taxbrackets WHERE ? >= married_start AND ? <= married_end', (taxable_income_itemized, taxable_income_itemized))
            tax_bracket = cursor.fetchone()

        # Calculate the tax amount based on the retrieved tax bracket and the taxable income
        tax_rate, _, _, _, _  = tax_bracket

        # Close the database connection and return the tax amount
        conn.close()
        
        to_view =[]
        return_Itemized = (taxable_income_itemized * tax_rate) - self.federal_tax
        to_view.append(tax_rate)
        to_view.append(return_Itemized)
        to_view.append(taxable_income_itemized)
        

        return to_view


    class Meta:
        app_label = 'CalApp'''

class Demographics(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    filling_status = models.CharField(max_length=255)

    # add other demographic fields as needed

class Income(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    gross_income = models.FloatField()

class Taxes(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    federal_tax = models.FloatField()

class Education(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    enrolled = models.BooleanField()
    college_expenses = models.FloatField()
    student_loan_interest = models.FloatField()
    scholarships_received = models.FloatField()

class Home(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    own = models.BooleanField()
    interest_taxes = models.FloatField()

class Vehicle(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    taxes_registration = models.FloatField()

class Medical(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    medical_expenses = models.FloatField()

class Charitable(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    charitable_contributions = models.FloatField()

class Retirement(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    retirement_contributions = models.FloatField()
