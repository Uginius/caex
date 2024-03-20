from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    crypto_exchange = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    foreign_exchange = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    bank_account = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    money_transfer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)

    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2'


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    crypto_exchange = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    foreign_exchange = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    bank_account = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)
    money_transfer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'ms-auto'}), required=False)

    class Meta:
        model = Profile
        fields = ['crypto_exchange', 'foreign_exchange', 'bank_account', 'money_transfer']
