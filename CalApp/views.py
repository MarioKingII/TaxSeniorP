from django.shortcuts import render, redirect
from .models import Demographics, Income, Taxes, Education, Home, Vehicle, Medical, Charitable, Retirement,  TaxCalculation
from .form import FillingStatusForm


# Create your views here.

def demographics_view(request):
    filling_status = None
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        form = FillingStatusForm(request.POST)
        if form.is_valid():
            filling_status = form.cleaned_data['filling_status']
            demographics = Demographics.objects.create(name=name, age=age, filling_status=filling_status )
            request.session['demographics_id'] = demographics.id
            return redirect(income_view)
    else:
        form = FillingStatusForm()        
    return render(request, 'demographics.html', {'filling_status': filling_status, 'form': form})

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
    college_expenses = 0
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
    interest_taxes = 0
    if request.method == 'POST':
        own = request.POST.get('own', False)
        interest_taxes = request.POST.get('interest_taxes')
        home = Home.objects.create(demographics_id=demographics_id, own=own, interest_taxes=interest_taxes)
        request.session['home_id'] = home.id
        return redirect(vehicle_view)
    return render(request, 'home.html')

def vehicle_view(request):
    demographics_id = request.session.get('demographics_id')
    taxes_registration = 0
    if request.method == 'POST':
        taxes_registration = request.POST['taxes_registration']
        vehicle = Vehicle.objects.create(demographics_id=demographics_id, taxes_registration=taxes_registration)
        request.session['vehicle_id'] = vehicle.id
        return redirect(medical_view)
    return render(request, 'vehicle.html')

def medical_view(request):
    demographics_id = request.session.get('demographics_id')
    medical_expenses = 0
    if request.method == 'POST':
        medical_expenses = request.POST['medical_expenses']
        medical = Medical.objects.create(demographics_id=demographics_id, medical_expenses=medical_expenses)
        request.session['medical_id'] = medical.id
        return redirect(charitable_view)
    return render(request, 'medical.html')

def charitable_view(request):
    demographics_id = request.session.get('demographics_id')
    charitable_contributions = 0 
    if request.method == 'POST':
        charitable_contributions = request.POST['charitable_contributions']
        charitable = Charitable.objects.create(demographics_id=demographics_id, charitable_contributions=charitable_contributions)
        request.session['charitable_id'] = charitable.id
        return redirect(retirement_view)
    return render(request, 'charitable.html')

def retirement_view(request):
    demographics_id = request.session.get('demographics_id')
    retirement_contributions =0
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
        demographics_id = request.session.get('demographics_id')
        charitable_id = request.session.get('charitable_id')
        education_id = request.session.get('education_id')
        home_id = request.session.get('home_id')
        vehicle_id = request.session.get('vehicle_id')
        medical_id = request.session.get('medical_id')
        retirement_id = request.session.get('retirement_id')
        charitable = Charitable.objects.get(id=charitable_id)
        education = Education.objects.get(id=education_id)
        home = Home.objects.get(id=home_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        medical = Medical.objects.get(id=medical_id)
        retirement = Retirement.objects.get(id=retirement_id)
        income = Income.objects.get(id=income_id)
        taxes = Taxes.objects.get(id=taxes_id)
        demographics = Demographics.objects.get(id=demographics_id)
        filling_status = demographics.filling_status
        gross_income = income.gross_income
        federal_tax = taxes.federal_tax
        charitable_contributions = charitable.charitable_contributions
        college_expenses = education.college_expenses
        taxes_registration = vehicle.taxes_registration
        interest_taxes = home.interest_taxes
        medical_expenses = medical.medical_expenses
        retirement_contributions = retirement.retirement_contributions
    
        calculation = TaxCalculation(
            gross_income=gross_income, 
            federal_tax=federal_tax, 
            filling_status=filling_status, 
            charitable_contributions=charitable_contributions,
            college_expenses=college_expenses,
            taxes_registration=taxes_registration, 
            interest_taxes=interest_taxes,
            medical_expenses=medical_expenses,
            retirement_contributions=retirement_contributions)
        
        tax_s = calculation.calculate_standard_tax()
        tax_i = calculation.calculate_itemized_tax()

        tax_rate_s, retun_stand, TS = tax_s
        tax_rate_i, return_itemized, TI = tax_i

        return render(request, 'result.html', {'retun_itemized': return_itemized,
                                            'retun_stand': retun_stand,
                                            'federal_tax': federal_tax,
                                            'filling_status':filling_status,
                                            'tax_rate_s':tax_rate_s,
                                            'tax_rate_i': tax_rate_i,
                                            'retirement_contributions':retirement_contributions,
                                            'charitable_contributions':charitable_contributions,
                                            'college_expenses':college_expenses,
                                            'taxes_registration':taxes_registration, 
                                            'interest_taxes':interest_taxes,
                                            'medical_expenses':medical_expenses,
                                            'TS':TS,
                                            'TI':TI})
    return render(request, 'result.html')