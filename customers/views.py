from multiprocessing import context
from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa
from django.views.generic import ListView, CreateView
from . import models
from . import forms
from django.urls import reverse_lazy
import pandas as pd
# Create your views here.

class CustomerListView(ListView):
    template_name = 'customer_list.html'
    model = models.Customer
    context_object_name = "customers"
    #paginate_by = 10


class CustomerCreateView(CreateView):
    template_name = 'create_customer.html'
    form_class = forms.CustomerForm
    success_url = reverse_lazy('customer-list')

    def get_success_url(self):
        return reverse("customers:customer-list")


'''
def customerhome(request):
    item = Customer.objects.all().values()
    # df = pd.DataFrame(item)
    # mydict = {
    #     "df": df.to_html()
    # }
    context = {
        'items' : item
    }
    return render(request, 'index.html', context)

'''

'''
class CustomerListView(ListView):
    model = Customer
    template_name = 'main.html'

'''

'''
def show(request):
    queryset = Customer.objects.all()
    context= {'customers': queryset}
    return render(request, "main.html", context)



def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)

    template_path = 'pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

'''
