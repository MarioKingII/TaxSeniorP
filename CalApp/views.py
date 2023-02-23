from django.shortcuts import render, redirect
from .models import Demographics, Income, Taxes, Education, Home, Vehicle, Medical, Charitable, Retirement,  TaxCalculation
from django.http import HttpResponse


# Create your views here.
'''def Home(request):
    return render(request, 'CalculateTax.html')

def result(request):
    return render(request, 'result.html')

def calculate_tax(request):
    if request.method == 'POST':
        income = float(request.POST['income'])
        tax_rate = float(request.POST['tax_rate'])
        calculation = TaxCalculation(income=income, tax_rate=tax_rate)
        tax = calculation.calculate_tax()
        return render(request, 'result.html', {'tax': tax})
    return render(request, 'CalculateTax.html')'''


def demographics_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        # add other demographic fields as needed
        demographics = Demographics.objects.create(name=name, age=age)
        request.session['demographics_id'] = demographics.id
        return redirect(income_view)
    return render(request, 'demographics.html')

def income_view(request):
    demographics_id = request.session.get('demographics_id')
    gross_income = 0 # Define gross_income here

    if request.method == 'POST':
        gross_income = request.POST['gross_income']
        income = Income.objects.create(demographics_id=demographics_id, gross_income=gross_income)
        request.session['income_id'] = income.id
        return redirect(taxes_view)
    return render(request, 'income.html', {'gross_income': gross_income })

def taxes_view(request):
    demographics_id = request.session.get('demographics_id')
    federal_tax = 0 # Define federal_tax here
    if request.method == 'POST':
        federal_tax = request.POST['federal_tax']
        taxes = Taxes.objects.create(demographics_id=demographics_id, federal_tax=federal_tax)
        request.session['taxes_id'] = taxes.id
        return redirect(education_view)
    return render(request, 'taxes.html', {'federal_tax': federal_tax})

def education_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        enrolled = request.POST.get('enrolled', False)
        college_expenses = request.POST.get('college_expenses')
        scholarships_received = request.POST.get('scholarships_received')
        education = Education.objects.create(demographics_id=demographics_id, enrolled=enrolled, college_expenses=college_expenses, scholarships_received=scholarships_received)
        request.session['education_id'] = education.id
        return redirect(home_view)
    return render(request, 'education.html')

def home_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        own = request.POST.get('own', False)
        interest_taxes = request.POST.get('interest_taxes')
        home = Home.objects.create(demographics_id=demographics_id, own=own, interest_taxes=interest_taxes)
        request.session['home_id'] = home.id
        return redirect(vehicle_view)
    return render(request, 'home.html')

def vehicle_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        taxes_registration = request.POST['taxes_registration']
        vehicle = Vehicle.objects.create(demographics_id=demographics_id, taxes_registration=taxes_registration)
        request.session['vehicle_id'] = vehicle.id
        return redirect(medical_view)
    return render(request, 'vehicle.html')

def medical_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        medical_expenses = request.POST['medical_expenses']
        medical = Medical.objects.create(demographics_id=demographics_id, medical_expenses=medical_expenses)
        request.session['medical_id'] = medical.id
        return redirect(charitable_view)
    return render(request, 'medical.html')

def charitable_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        charitable_contributions = request.POST['charitable_contributions']
        charitable = Charitable.objects.create(demographics_id=demographics_id, charitable_contributions=charitable_contributions)
        request.session['charitable_id'] = charitable.id
        return redirect(retirement_view)
    return render(request, 'charitable.html')

def retirement_view(request):
    demographics_id = request.session.get('demographics_id')
    if request.method == 'POST':
        retirement_contributions = request.POST['retirement_contributions']
        retirement = Retirement.objects.create(demographics_id=demographics_id, retirement_contributions=retirement_contributions)
        request.session['retirement_id'] = retirement.id
        return redirect(result)
    return render(request, 'retirement.html')

def result(request):
    if request.method == 'GET':
        income_id = request.session.get('income_id')
        taxes_id = request.session.get('taxes_id')
        income = Income.objects.get(id=income_id)
        taxes = Taxes.objects.get(id=taxes_id)
        gross_income = income.gross_income
        federal_tax = taxes.federal_tax
        #standard_deduction = 12200
        calculation = TaxCalculation(gross_income=gross_income, federal_tax=federal_tax)
        tax = calculation.calculate_tax()
        #tax = float(gross_income) - float(federal_tax) - float(standard_deduction)
        return render(request, 'result.html', {'tax': tax,'federal_tax': federal_tax})
    return render(request, 'result.html')