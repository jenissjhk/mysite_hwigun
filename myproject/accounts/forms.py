from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    관심지역 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', '관심지역', 'password1', 'password2',]