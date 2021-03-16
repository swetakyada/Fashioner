from django.urls import path,include

# from .views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    # path('logout/',TemplateView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup_view, name="signup"),
	path('', views.login, name="login"),  
	path('logout/', views.logout, name="logout"),
]