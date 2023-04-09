from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostModel, UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class ProfilePicForm(forms.ModelForm):

    pic = forms.ImageField(widget=forms.FileInput(attrs={"class":"imginput"}))
    class Meta:
        model = UserProfile
        fields = ['pic']

class PostFrom(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'description']