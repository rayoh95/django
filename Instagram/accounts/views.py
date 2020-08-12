from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
            return render(request, 'accounts/signup_complete.html')
        else:
            return render(request, 'accounts/signup_pwError.html')

    return render(request, 'accounts/signup.html')

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) 

        if user is not None:
            auth.login(request, user)
            return redirect('Boards:boards')
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('Boards:boards')