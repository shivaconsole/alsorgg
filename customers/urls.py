from django.urls import path
from .views import  customerhome
#render_pdf_view, CustomerListView, customer_render_pdf_view
app_name = 'customers'

urlpatterns = [
    path('', customerhome, name='customer-list-view'),
    #path('', CustomerListView.as_view(), name='customer-list-view'),
    #path('test/', render_pdf_view, name='test-view'),
    #path('pdf/<pk>/', customer_render_pdf_view, name='customer-pdf-view')

]