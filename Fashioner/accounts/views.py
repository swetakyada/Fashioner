from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('')
    template_name = 'registration/login.html'

def index(request):
    if request.user.is_authenticated:
        render(request,'home',context=None)
    else:
        print("Not logged in")

