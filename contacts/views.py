from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms
from django.urls import reverse_lazy
# Create your views here.
class ContactListView(ListView):
    template_name = 'contact_list.html'
    model = models.Contact
    context_object_name = "contacts"
    #paginate_by = 10

    #def get_context_data(self, *, object_list=None, **kwargs):


class ContactCreateView(CreateView):
    template_name = 'create_contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('contact-list')

    def get_success_url(self):
        return reverse("contacts:contact-list")

