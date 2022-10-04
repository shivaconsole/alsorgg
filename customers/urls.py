from django.urls import path
from . import views
#render_pdf_view, CustomerListView, customer_render_pdf_view
app_name = 'customers'

urlpatterns = [
    #path('', customerhome, name='customer-list-view'),
    path('', views.CustomerListView.as_view(), name='customer-list'),
    path('create/', views.CustomerCreateView.as_view(), name='customers'),

    #path('', CustomerListView.as_view(), name='customer-list-view'),
    #path('test/', render_pdf_view, name='test-view'),
    #path('pdf/<pk>/', customer_render_pdf_view, name='customer-pdf-view')

]