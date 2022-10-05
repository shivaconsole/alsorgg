"""alsorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
import imp
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from leads.views import landing_page, SignupView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.views.static import serve
from django.conf.urls import url
from quotations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page),
#path('dashboard/', include('leads.urls',  namespace='dashboard')),
    path('leads/', include("leads.urls", namespace='leads')),
   # path('leads/create'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('quotations/', include("quotations.urls", namespace='quotations')),
    path('contacts/', include("contacts.urls", namespace='contacts')),
    path('customers/', include("customers.urls", namespace='customers')),
    path('reports/', include('reports.urls')),

    path('quotations/create/addBlockItem', views.addBlockItem),
    path('quotations/create/addFitting', views.addFitting),
    path('quotations/create/addAppliance', views.addAppliance),
    path('quotations/create/discounts', views.discounts),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)