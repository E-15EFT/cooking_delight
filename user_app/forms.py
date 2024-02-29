# forms.py

from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


# Default user creation form
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password (again)",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
# Default authentication form
class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )
# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
