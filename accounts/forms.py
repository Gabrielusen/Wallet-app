from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# from django.forms.widgets import PasswordInput, TextInput, EmailInput, FileInput, NumberInput


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required fields and repeated password
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    """
    A form to update users. includes all fields on users
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
