
from django import forms
from PIL import Image


class Register(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    age = forms.CharField(max_length=3, required=True)
    address = forms.CharField(max_length=75, required=True)
    phonenumber = forms.CharField(max_length=20, required=False)
    image = forms.ImageField(required=False)
    email = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)


class Login(forms.Form):

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
