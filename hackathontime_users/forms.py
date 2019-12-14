from django import forms
from django.contrib.auth.models import User
from .models import Profile, Team #, Post
from django.contrib.auth.forms import UserCreationForm
from colleges import *
from django.db import models
from pagedown.widgets import PagedownWidget


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, label="E-Mail")
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), (
        "O", "Others"), ("X", "Prefer not to say")])

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'gender', 'username', 'email')

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=[('F', 'Female'), ('M', 'Male'), (
        "O", "Others"), ("X", "Prefer not to say")])

    class Meta:
        model = Profile
        fields = ['gender']

class CreateTeamForm(forms.ModelForm):
    team_name = forms.CharField(max_length=20, label="Team Name")

    class Meta:
        model = Team
        fields = ['team_name']

# class UserUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model=User
# 		fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=PagedownWidget(),
                          label="Bio (Pagedown/Markdown)", required=False)
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['bio', 'image']


class TeamOverviewForm(forms.ModelForm):
    team_overview = forms.CharField(widget=PagedownWidget(), label="Edit your team overview (Pagedown/Markdown)")

    class Meta:
        model = Team
        fields = ['team_overview']

# class CreatePostForm(forms.ModelForm):
#     title = forms.CharField(max_length=200, label="Title")
#     content = forms.CharField(widget=PagedownWidget(), label="Content (Pagedown/Markdown)")

#     class Meta:
#         model = Post
#         fields = ['title', 'content']