from django import forms
from django.contrib.auth.forms import UserCreationForm	
from django.contrib.auth.models import User


class UserRegisterforms(UserCreationForm):
	email = forms.EmailField()
	phonenumber = forms.CharField(max_length=10)

	class Meta:
		model = User
		fields = [ 'username', 'email','phonenumber', 'password1','password2']