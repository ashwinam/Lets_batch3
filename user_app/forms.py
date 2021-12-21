from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User 
from .models import Profile 

class SignUP(UserCreationForm):
	email = forms.EmailField(label ="Email")

	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):  # For auth_user table 
	class Meta:
		model = User 
		fields = ['email']

class ProfileUpdateForm(forms.ModelForm):  # for profile model or table 
	class Meta:
		model = Profile 
		fields = ['age', 'image']




