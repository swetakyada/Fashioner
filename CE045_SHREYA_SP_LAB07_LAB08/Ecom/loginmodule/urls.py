from django.urls import path
from .views import login, auth_view, logout,loggedin, invalidlogin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
        url(r'^auth/$', auth_view),
        path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
        path('logout/', TemplateView.as_view(template_name='logout.html'), name='logout'),
        path('loggedin/', TemplateView.as_view(template_name='loggedin.html'), name='loggedin'),
        path('invalidlogin/', TemplateView.as_view(template_name='invalidlogin.html'), name='invalidlogin'),
    ]