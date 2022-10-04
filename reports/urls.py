from django.urls import path
# from .views import reportHome
from . import views
app_name = 'reports'

urlpatterns = [
    path('', views.reportHome, name='reportHome'),
    path('reportEntry', views.reportEntry, name='reportEntry'),
    
]