from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class CreationUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords not matches')
        return cd['password2']

    def clean_email(self):
        cd=self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('this email already registered before')
        return cd['email']
    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('this name already registered before , try again')
        return cd['username']