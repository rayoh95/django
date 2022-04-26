from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.

# 회원가입
def signup(request):
    
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
            return render(request, 'accounts/signup_complete.html')
        else:
            return render(request, 'accounts/signup_pwError.html')

    return render(request, 'accounts/signup.html')

# 로그인 기능
def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) 

        if user is not None:
            auth.login(request, user)
            return redirect('posts:posts')
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        return render(request,'accounts/login.html')

# 로그아웃 기능
def logout(request):
    auth.logout(request)
    return redirect('posts:index')

# 팔로우 기능
def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id=user_id)

    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)

    return redirect('posts: posts')