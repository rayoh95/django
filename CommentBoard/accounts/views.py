from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:      #password1,2 가 같다면,
            User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])   #입력한 username 과 password 로 user 를 생성한다.
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/signup_pwError.html')

    return render(request, 'accounts/signup.html')

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #사용자한테 입력받은 username 과 password 를 user 에 저장한다.

        if user is not None:    # 그 user 가 있는지 없는지 판별
            auth.login(request, user)
            return redirect('Boards:boards')
        else:
            return render(request, 'accounts/login_error.html')
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('Boards:boards')
