from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='FirstName')
    last_name = forms.CharField(max_length=100, help_text='LastName')
    email = forms.EmailField(max_length=150, help_text='Email')
    phone_no=forms.CharField(max_length=10,help_text='mobile no')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','phone_no', 'password1', 'password2',)

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.userprofile.first_name = form.cleaned_data.get('first_name')
        user.userprofile.last_name = form.cleaned_data.get('last_name')
        user.userprofile.email = form.cleaned_data.get('email')
        user.userprofile.phone = form.cleaned_data.get('phone')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        request.session["user"] = user
        login(request, user)
        return redirect('home-page.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
# def signup(request):
#     form=CreateUserForm()
#     if request.method=='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid:
#             form.save()
#     context={'form':form}
#     return render(request,'registration/signup.html',context)

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def Logout(request):
    logout(request)
    return redirect(reverse_lazy('FashionerMain:logout'))


