from django.db import models

class TaxCalculation(models.Model):
    gross_income = models.FloatField()
    federal_tax = models.FloatField()
    standard_deduction = 12200

    def calculate_tax(self):
        NetIncome = self.gross_income - self.federal_tax - self.standard_deduction
        return NetIncome * 0.10

    class Meta:
        app_label = 'CalApp'''

class Demographics(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
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
    college_expenses = models.FloatField(blank=True, null=True)
    scholarships_received = models.FloatField(blank=True, null=True)

class Home(models.Model):
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    own = models.BooleanField()
    interest_taxes = models.FloatField(blank=True, null=True)

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
