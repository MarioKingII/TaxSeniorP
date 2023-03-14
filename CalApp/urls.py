from django.urls import path
from . import views


urlpatterns = [
    path('demographics/', views.demographics_view),
    path('income/', views.income_view),
    path('taxes/', views.taxes_view),
    path('education/', views.education_view),
    path('home/', views.home_view),
    path('vehicle/', views.vehicle_view),
    path('medical/', views.medical_view),
    path('charitable/', views.charitable_view),
    path('retirement/', views.retirement_view),
    path('result/', views.result)
]