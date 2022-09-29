from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import forms
#from .models import *
from .models import Lead, Agent
from django.views import generic
from .forms import LeadForm, CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

def landing_page(request):
    return render(request, 'landing.html')

class LeadListView(ListView):

    template_name = 'lead_list.html'
    model = models.Lead
    context_object_name = "leads"


    #paginate_by = 10

   # def get_context_data(self, *, object_list=None,):

'''
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "lead_list.html", context)
'''

'''
class LeadDetailView(DetailView):

    model = Lead
    template_name = 'lead_detail.html'

    def get_context_data(self, lead):
        # Call the base implementation first to get a context
        context = super(LeadDetailView, self).get_context_data()
        # Add in a QuerySet of all the books
        context['leads'] = Lead.objects.filter(lead_id=id, status=True)
        return context
    
    
'''
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, "lead_detail.html", context)

class LeadCreateView(CreateView):
    template_name = 'create_lead.html'
    form_class = forms.LeadForm
    success_url = reverse_lazy('lead-list')

    def get_success_url(self):
        return reverse("leads:lead-list")




'''
    def get_success_url(self):
        return reverse("leads/create/")
'''
'''
def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        print('Receiveing a post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            #lead_name = form.cleaned_data['lead_name']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            #lead_id = id
            #primary_email = form.cleaned_data['primary_email']
            Contactno = form.cleaned_data['Contactno']
            address = form.cleaned_data['address']
            #BelongsToUnit = form.cleaned_data['BelongsToUnit']
            #Budget = form.cleaned_data['Budget']
            #Probability = form.cleaned_data['Probability']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                #primary_email=primary_email,
                #Budget=Budget,
                #Address=Address,
                #Probability=Probability,
                agent=agent
            )
            print('The lead has been created')
            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "create_lead.html ", context)
'''
class PasswordResetView():
    pass

class PasswordResetDoneView():
    pass

def lead_delete(request):
    pass

def lead_update(request):
    pass


    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this lead")
        return super(LeadUpdateView, self).form_valid(form)
