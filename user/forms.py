from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model,authenticate
from django.utils.html import strip_tags
from django.core.validators import RegexValidator

User=get_user_model()
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,max_length=100,
                             widget=forms.EmailInput(attrs={'class':'form-control'}))