from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insurance/<int:insurance_id>/', views.insurance_detail, name='insurance_detail'),
]
