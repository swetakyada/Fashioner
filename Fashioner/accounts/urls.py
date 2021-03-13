from django.urls import path,include

from .views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    # path('logout/',LogoutView.as_view(), name='logout')
]