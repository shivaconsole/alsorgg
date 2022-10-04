from django import forms
from .models import Quotation
#from alsorg.leads.models import Belongstounit
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
class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'

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
'''
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

'''