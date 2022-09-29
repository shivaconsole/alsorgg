from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

User = get_user_model()
'''
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'lead_name',
            'first_name',
            'last_name',
            'primary_email',
            'Contactno',
            'Address',
            'BelongsToUnit',
            'Budget',
            'Probability',
            'agent'
        )
'''

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'





'''
    lead_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    salutaion = forms.CharField()
    primary_email = forms.CharField()
    Contactno = forms.CharField()
    Address = forms.CharField()
    lead_state = 
    BelongsToUnit = forms.CharField()
    Budget = forms.CharField()
    Probability = forms.IntegerField(min_value=0)
'''


    #LeadState
    #LeadStatusCode
    #ProductGroup
    #Category
    #CategoryCode
    #State
    #City
    #Country
    #Source
    #SourceCategory

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

