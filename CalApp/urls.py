from django.urls import path
from . import views


urlpatterns = [
    path('demographics/', views.demographics_view, name='demographics_view'),
    path('income/', views.income_view, name='income_view'),
    path('taxes/', views.taxes_view, name='taxes_view'),
    path('education/', views.education_view, name='education_view'),
    path('home/', views.home_view, name='home_view'),
    path('vehicle/', views.vehicle_view, name='vehicle_view'),
    path('medical/', views.medical_view, name='medical_view'),
    path('charitable/', views.charitable_view, name='charitable_view'),
    path('retirement/', views.retirement_view, name='retirement_view'),
    path('result/', views.result, name='result'),
]
