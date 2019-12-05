from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm, ProfileUpdateForm, UserUpdateForm, CreateTeamForm
from django.contrib.auth.decorators import login_required
from .models import Team, Profile
from PIL import Image


def register(request):
	if request.user.is_authenticated:
		return redirect('ht-home')
	if request.method == "POST":
		user_form = UserForm(request.POST)
		# profile_form = ProfileForm(request.POST)

		if user_form.is_valid(): #and profile_form.is_valid():
			user_form.save()
			# profile_form.save()
			username = user_form.cleaned_data.get('username')
			messages.success(request, f"Account for username \"{username}\" has been created. Login to your new account.")
			return redirect('ht-login')
		else:
			messages.warning(request, 'Please correct the errors below.')
	else:
		user_form = UserForm(initial={'max_number': '3'})
		# profile_form = ProfileForm()

	return render(request, 'hackathontime_users/register.html', {'user_form':user_form}) #, 'profile_form':profile_form})

@login_required
def profile(request):
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			# image check
			print(profile_form.cleaned_data.get('image').name)
			curr_image = Image.open(profile_form.cleaned_data.get('image'))
			if curr_image.height < 295 or curr_image.width < 295:
				messages.warning(request, 'Image must be larger than 300x300 pixels.')
				curr_image.close()
				return redirect('ht-profile')
			
			curr_image.close()

			# save form
			user_form.save()
			profile_form.save()
			username = user_form.cleaned_data.get('username')
			messages.success(request, f"Account successfully updated for {username}'s profile!")
			return redirect('ht-profile')
		else:
			messages.warning(request, 'Please correct the errors below.')
			return redirect('ht-profile')

	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
		team_members = Profile.objects.filter(team=request.user.profile.team)

	context = {
		'user_form' : user_form,
		'profile_form' : profile_form,
		'team_members': team_members,
	}

	return render(request, 'hackathontime_users/profile.html', context)

@login_required
def register_team(request):
	if Profile.objects.get(user=request.user).is_in_a_team:
		messages.warning(request, "You're already in a team.")
		return redirect('ht-profile')

	# theres no need for another query ig
	# request.user.profile.is_in_a_team should also work
	# TODO ^
	if request.method == "POST":
		team_form  = CreateTeamForm(request.POST)

		if team_form.is_valid():
			team_instance = team_form.save()
			profile = Profile.objects.get(user=request.user)
			profile.team = team_instance
			profile.is_in_a_team = True
			profile.save()
			# request.user.profile.team = team_form
			# request.user.profile.save()
			team_name = team_form.cleaned_data.get('team_name')
			messages.success(request, f"Team '{team_name}' successfully created!")
			return redirect('ht-profile')
		else:
			messages.warning(request, 'Please correct the errors below.')
			return redirect('ht-profile')
	else:
		team_form  = CreateTeamForm()

	context = {
		'team_form': team_form,
	}

	return render(request, 'hackathontime_users/register_team.html', context)
