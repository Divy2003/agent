from django.contrib import admin
from .models import Agent, Insurance, InsuranceCompany, InsurancePlan

admin.site.register(Agent)
admin.site.register(Insurance)
admin.site.register(InsuranceCompany)
admin.site.register(InsurancePlan)