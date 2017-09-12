from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Имя пользователя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', required=True, error_messages='')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')