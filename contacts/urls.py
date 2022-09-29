from django.urls import path
from . import views

from django.urls import path, include
from .views import *
#lead_list, lead_detail, lead_create, lead_delete, lead_update
from django.contrib.auth.decorators import login_required
app_name = "contacts"

urlpatterns = [
    #path('', lead_list, name='lead-list'),
    path('', login_required(views.ContactListView.as_view()), name='contact-list'),
    #path('<int:pk>/', lead_detail),
    #path('<int:pk>/', login_required(views.LeadDetailView.as_view()), name='lead-detail'),
    #path('create/', lead_create),
    path('create/', ContactCreateView.as_view(), name='contacts'),
    #path('<int:pk>/delete', lead_delete),
    #path('<int:pk>/update', lead_update),
]