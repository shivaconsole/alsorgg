from django.urls import path
from . import views

from django.urls import path, include
from .views import *
#lead_list, lead_detail, lead_create, lead_delete, lead_update
from django.contrib.auth.decorators import login_required
app_name = "leads"

urlpatterns = [
    #path('', lead_list, name='lead-list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', login_required(views.LeadListView.as_view()), name='lead-list'),
    path('<int:pk>/', lead_detail),
    #path('<int:pk>/', login_required(views.LeadDetailView.as_view()), name='lead-detail'),
    #path('create/', lead_create),
    path('create/', LeadCreateView.as_view(), name='leads'),
    path('<int:pk>/delete', lead_delete),
    path('<int:pk>/update', lead_update),
]