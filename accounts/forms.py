from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from accounts.models import User
from accounts.utils import send_email_for_verify


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
