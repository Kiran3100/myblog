from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from blog.models import PostModel
from django.utils import timezone

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username' : 'Username',
            'first_name' : 'Firstname',
            'last_name' : 'Lastname',
            'email' : 'Email',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'
        exclude = ['user_name']

class UpdateUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels = {
            'username' : 'Username',
            'first_name' : 'Firstname',
            'last_name' : 'Lastname',
            'email' : 'Email',
            'date_joined' : 'DateJoined',
            'last_login' : 'Lastlogin',
            'is_active' : 'Isactive',
        }

class UpdateAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username' : 'Username',
            'first_name' : 'Firstname',
            'last_name' : 'Lastname',
            'email' : 'Email',
            'date_joined' : 'DateJoined',
            'last_login' : 'Lastlogin',
            'is_active' : 'Isactive',
        }
