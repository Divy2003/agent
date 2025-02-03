from django.shortcuts import render, get_object_or_404
from .models import Agent, Insurance, InsuranceCompany, InsurancePlan

def home(request):
    agent = Agent.objects.first()  # Assuming only one agent
    insurances = Insurance.objects.all()
    return render(request, 'agent/home.html', {'agent': agent, 'insurances': insurances})

def insurance_detail(request, insurance_id):
    insurance = get_object_or_404(Insurance, id=insurance_id)
    plans = InsurancePlan.objects.filter(insurance=insurance)
    agent = Agent.objects.first()
    return render(request, 'agent/insurance_detail.html', {
        'insurance': insurance,
        'plans': plans,
        'agent': agent
    })