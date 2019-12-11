from django import forms
from django.contrib.auth.models import User
from .models import Profile, Team
from django.contrib.auth.forms import UserCreationForm
from colleges import *
from django.db import models
from pagedown.widgets import PagedownWidget

class UserForm(UserCreationForm):
	email = forms.EmailField(max_length=255, label="E-Mail")
	first_name = forms.CharField(max_length=255, label="First Name")
	last_name = forms.CharField(max_length=255, label="Last Name")
	class Meta:
		model=User
		# fields = '__all__'
		fields = ('first_name', 'last_name', 'username', 'email')

class CreateTeamForm(forms.ModelForm):
	team_name = forms.CharField(max_length=20, label="Team Name")
	class Meta:
		model=Team
		fields = ['team_name']

# class UserUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model=User
# 		fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
	bio = forms.CharField(widget=PagedownWidget(), label="Bio (Pagedown/Markdown)", required=False)
	image = forms.ImageField(required=False, widget=forms.FileInput)
	class Meta:
		model=Profile
		fields = ['bio','image']