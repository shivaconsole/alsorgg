from django.db import models
from .constants import *
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models

class User(AbstractUser):
    pass

class Category(models.Model):
    pass

class ProductCategory(models.Model):
    product_group = models.CharField(max_length=100, choices=PRODUCT_GROUP)
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_category

class LeadStatusCode(models.Model):
    lead_status = models.CharField(max_length=100, choices=LEAD_STATE)
    status_code = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.status_code

class LeadCategoryCode(models.Model):
    lead_category_code = models.CharField(max_length=100, choices=LEAD_CATEGORY)
    lead_category = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.lead_category_code


class Belongstounit(models.Model):
    unit_type = models.CharField(max_length=20, choices=CHOICES_BU, null=True, blank=True, default=None)

    def __str__(self):
        return self.unit_type

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salutation = models.CharField(max_length=20, choices=CHOICES_SAL)
    email_id = models.EmailField(max_length=40, default=None, null=True)
    contactno = models.CharField(max_length=15, default=None, null=True)
    address = models.TextField()
    landmark = models.CharField(max_length=50)
    budget = models.CharField(max_length=20, default=None, null=True),
    #probability = models.CharField(max_length=10, default=None, null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    lead_state = models.CharField(max_length=100, choices=LEAD_STATE, default=None, null=True)
    lead_status_code = models.ForeignKey(LeadStatusCode, on_delete=models.SET_NULL, default=None, null=True)
    product_group = models.CharField(max_length=100, choices=PRODUCT_GROUP, default=None, null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, default=None, null=True)
    #belongs_to_unit = models.ForeignKey(Belongstounit, max_length=20, choices=CHOICES_BU, null=True, default=None, on_delete=models.SET_DEFAULT)
    #lead_category = models.ForeignKey(LeadCategoryCode, choices=LEAD_CATEGORY, on_delete=models.SET_NULL, default=None, null=True)
    #3 product_group =



    def __str__(self):
        return f"{self.salutation} {self.first_name} {self.last_name}"
'''
    def get_absolute_url(self):
        return reverse('lead-list', kwargs={'pk': self.pk})'''

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username











'''


class Member(models.Model):

    residing_country = models.CharField(max_length=50)
    residing_state = models.CharField(max_length=50)
    residing_city = models.CharField(max_length=50)

class Country(models.Model):

    country = models.CharField(max_length=20)

class State(models.Model):

    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):

    city=models.CharField(max_length=20)
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    
'''
