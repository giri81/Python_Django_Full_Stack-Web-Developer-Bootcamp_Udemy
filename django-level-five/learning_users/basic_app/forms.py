from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModeForm):

    password = forms.CharField(widget=PasswordInput())

    class Meta():

        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
         
