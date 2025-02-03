from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='agents/', default='default_agent.jpg')
    bio = models.TextField(default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return self.name

class Insurance(models.Model):
    INSURANCE_TYPES = [
        ('LIFE', 'Life Insurance'),
        ('HEALTH', 'Health Insurance'),
        ('HOME', 'Home Insurance'),
        ('AUTO', 'Auto Insurance'),
        ('BUSINESS', 'Business Insurance'),
    ]
    
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=INSURANCE_TYPES, default='LIFE')
    description = models.TextField(default='')
    image = models.ImageField(upload_to='insurance/', default='default_insurance.jpg')

    def __str__(self):
        return f"{self.get_type_display()} - {self.title}"

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='companies/', default='default_company.jpg')
    description = models.TextField(default='')
    website = models.URLField(blank=True, default='')
    
    def __str__(self):
        return self.name

class InsurancePlan(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='plans')
    company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    features = models.TextField(default='')
    price_range = models.CharField(max_length=100, default='Contact for pricing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.name}"