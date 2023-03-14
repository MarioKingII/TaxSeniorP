from django import forms

class FillingStatusForm(forms.Form):
    
    FILLING_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Single', 'Married'),
    )
    filling_status = forms.ChoiceField(choices=FILLING_STATUS_CHOICES)