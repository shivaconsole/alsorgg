from django.shortcuts import render, reverse
from .models import Appliance, AppliancekDiscount, Fitting, FittingDiscount, OtherDiscount, PackingDiscount, Quotation, BlockItem, WoodworkDiscount
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from . import forms
from django.views.generic import ListView
from django.http import HttpResponseRedirect

import pandas as pd
# Create your views here.
def quotation_list(request):
    quotation = Quotation.objects.all().values()
    # df = pd.DataFrame(quotation)
    # mydict = {
    #     "df": df.to_html
    # }
    context = {
        'quotations' : quotation
    }
    return render(request, "quotations_list.html", context)

'''
 item = Student.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'index.html', context=mydict)
'''
def quotation_detail(request, pk):
    quotation = Quotation.objects.get(id=pk)
    context = {
        'quotation': quotation
    }
    return render(request, "quotation_detail.html", context)

class QuotationCreateView(CreateView):
    template_name = 'create_quotation.html'
    form_class = forms.QuotationForm
    success_url = reverse_lazy('quotation')

    def get_success_url(self):
        return reverse("quotations:quotation-list")

class QuotationUpdateView(UpdateView):
    template_name = 'quotation/form.html'
    model = models.Quotation
    form_class = forms.QuotationForm
    success_url = reverse_lazy('quotation')

class QuotationListView(ListView):
    template_name = 'quotation_list.html'
    model = models.Quotation
    paginate_by = 10


def showdata(request):
    queryset = Quotation.objects.all()
    context = {'clientes': queryset}

    return render(request, 'quotations_list.html', context)

def addBlockItem(request):
    if request.method == 'POST':
        desc = request.POST['desc']
        finish = request.POST['finish']
        unit = request.POST['unit']
        width = request.POST['width']
        height = request.POST['height']
        qty = request.POST['qty']
        rate = request.POST['rate']
        payType = request.POST['payType']
        refImg = request.FILES['refImg']

        blockVal = BlockItem(desc=desc, finish=finish, unit=unit, width=width, height=height, qty=qty,rate=rate,payType=payType, img=refImg)
        blockVal.save()
        return HttpResponseRedirect('/quotations/create/')

    return render(request, 'create_quotation.html')

def addFitting(request):
    if request.method == "POST":
        brand = request.POST['brand']
        desc = request.POST['desc']
        unit = request.POST['unit']
        price = request.POST['price']
        qty = request.POST['qty']
        payType = request.POST['payType']
        refImg = request.FILES['refImg']
        fittinfVal = Fitting(brand=brand, desc=desc, unit=unit,price=price, qty=qty, payType=payType,img=refImg)
        fittinfVal.save()
        return HttpResponseRedirect('/quotations/create/')

    return render(request, 'create_quotation.html')

def addAppliance(request):
    if request.method == "POST":
        brand = request.POST['brand']
        desc = request.POST['desc']
        unit = request.POST['unit']
        price = request.POST['price']
        qty = request.POST['qty']
        payType = request.POST['payType']
        refImg = request.FILES['refImg']
        applianceVal = Appliance(brand=brand, desc=desc, unit=unit,price=price, qty=qty, payType=payType,img=refImg)
        applianceVal.save()
        return HttpResponseRedirect('/quotations/create/')
        
    return render(request, 'create_quotation.html')

def discounts(request):
    if request.method == "POST":
        wType = request.POST['wType']
        wValue = request.POST['wValue']        
        wPercent = request.POST['wPercent']        
        aType = request.POST['aType']        
        aValue = request.POST['aValue']        
        aPercent = request.POST['aPercent']        
        fType = request.POST['fType']        
        fValue = request.POST['fValue']        
        fPercent = request.POST['fPercent']        
        pType = request.POST['pType']        
        pValue = request.POST['pValue']        
        pPercent = request.POST['pPercent']        
        cartage = request.POST['cartage']        
        installation = request.POST['installation']        
        special_dis = request.POST['special_dis']
        woodValue = WoodworkDiscount(wType=wType, wValue=wValue, wPercent=wPercent)
        aplnceValue = AppliancekDiscount(aType=aType, aValue=aValue, aPercent=aPercent)
        fittValue = FittingDiscount(fType=fType, fValue=fValue, fPercent=fPercent)
        packValue = PackingDiscount(pType=pType, pValue=pValue, pPercent=pPercent)
        othrValue = OtherDiscount(cartage=cartage, installation=installation, special_dis=special_dis)    
        woodValue.save()
        aplnceValue.save()
        fittValue.save()
        packValue.save()
        othrValue.save()
        return HttpResponseRedirect('/quotations/create/')

    return render(request, 'create_quotation.html')


