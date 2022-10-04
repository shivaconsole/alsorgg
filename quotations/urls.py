from django.urls import path
from .views import quotation_list, QuotationCreateView, quotation_detail
from quotations import views


app_name = "quotations"

urlpatterns = [
    path('', quotation_list, name='quotation-list'),
    #path('createquotation/', quotation_create),
    path('<int:pk>/', quotation_detail),
    path('create/', QuotationCreateView.as_view()),
    # path('', views.addBlockItem, name='addBlockItem')
]