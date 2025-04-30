from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'phone', 'interests', 'photo']
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 4}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
