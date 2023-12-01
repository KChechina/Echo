from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Buyer
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
