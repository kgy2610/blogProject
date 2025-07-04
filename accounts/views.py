# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def main_page(request):
    return render(request, 'accounts/main.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main_page')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            nickname = form.cleaned_data['nickname']

            if User.objects.filter(username=nickname).exists():
                form.add_error('nickname', '이미 존재하는 닉네임입니다.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', '이미 등록된 이메일입니다.')
            else:
                user = User.objects.create_user(
                    username=nickname,
                    email=email,
                    password=password,
                    first_name=name
                )
                # phone 번호는 User 기본 모델에 없으므로 로그나 별도 처리 필요 (지금은 로그로 표시)
                print(f"전화번호: {phone}")
                return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})