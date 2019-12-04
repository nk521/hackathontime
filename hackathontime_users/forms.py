from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from colleges import *
from django.db import models

class UserForm(UserCreationForm):
	email = forms.EmailField(max_length=255, label="E-Mail")
	first_name = forms.CharField(max_length=255, label="First Name")
	last_name = forms.CharField(max_length=255, label="Last Name")
	class Meta:
		model=User
		# fields = '__all__'
		fields = ('first_name', 'last_name', 'username', 'email')

# class ProfileForm(forms.ModelForm):
# 	user_college = forms.ChoiceField(choices=colleges_list, label="College")
# 	user_state = forms.CharField(max_length=50, label="State/UT") # TODO: change this to choices

# 	class Meta:
# 		model = Profile
# 		fields = ('user_college', 'user_state')

# class CreateTeamForm(for)

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(max_length=255, label="E-Mail")
	class Meta:
		model=User
		fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['image']