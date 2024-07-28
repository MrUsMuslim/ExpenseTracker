# Django files
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Others
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    User Creation Form
    """

    email = forms.EmailField()
    
    class Meta:
        model = User
        fields: list[str] = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    User Update form
    """

    email = forms.EmailField()
    
    class Meta:
        model = User
        fields: list[str] = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    User Update form
    """

    class Meta:
        model = Profile
        fields: list[str] = ['full_name', 'image']