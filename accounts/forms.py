# accounts/forms.py
from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(
        label='이름',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': '이름 입력',
            'class': 'login-input'
        })
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(attrs={
            'placeholder': '이메일 입력',
            'class': 'login-input'
        })
    )
    phone = forms.CharField(
        label='전화번호',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '전화번호 입력',
            'class': 'login-input'
        })
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={
            'placeholder': '비밀번호 입력',
            'class': 'login-input'
        })
    )
    nickname = forms.CharField(
        label='닉네임',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': '닉네임 입력',
            'class': 'login-input'
        })
    )
