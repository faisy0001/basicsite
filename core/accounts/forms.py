from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email' , max_length=150, help_text='Email')
    password1 = forms.CharField(label='Password', max_length=255 , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password' , max_length=255 ,widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username',
'email', 'password1', 'password2',)