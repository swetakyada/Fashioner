from django.urls import path,include

from .views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import TemplateView


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('logout/',LogoutView.as_view(), name='logout')
]