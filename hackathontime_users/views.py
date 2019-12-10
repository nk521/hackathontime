from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, ProfileUpdateForm, CreateTeamForm
from django.contrib.auth.decorators import login_required
from .models import Team, Profile
from PIL import Image
from hackathontime_main.models import Hackathon

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
		user_form = UserForm()
		# profile_form = ProfileForm()

	return render(request, 'hackathontime_users/register.html', {'user_form': user_form}) #, 'profile_form': profile_form})

@login_required
def profile(request):
	if request.method == "POST":
		# user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		# if user_form.is_valid() and profile_form.is_valid():
		if profile_form.is_valid():
			# image check
			# print(profile_form.cleaned_data.get('image').name)
			curr_image = Image.open(profile_form.cleaned_data.get('image'))
			if curr_image.height < 295 or curr_image.width < 295:
				messages.warning(request, 'Image must be larger than 300x300 pixels.')
				curr_image.close()
				return redirect('ht-profile')
			

			# save form
			# user_form.save()
			profile_form.save()
			curr_image.close()
			# username = user_form.cleaned_data.get('username')
			messages.success(request, f"Account successfully updated for {request.user.username}'s profile!")
			return redirect('ht-profile')
		else:
			messages.warning(request, 'Please correct the errors below.')
			return redirect('ht-profile')

	else:
		# user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
		team_members = Profile.objects.filter(team=request.user.profile.team)

	context = {
		# 'user_form' : user_form,
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


@login_required
def profile_view(request, **kwargs):
	slug = kwargs['profile_slug']
	if request.user.profile.slug == slug:
		return redirect('ht-profile')

	profile_object = Profile.objects.filter(user__profile__slug=slug)
	if profile_object:
		profile_object = profile_object[0]
		team_members = Profile.objects.filter(team=profile_object.team)

		context={
			'profile': profile_object,
			'team_members': [str(team_member) for team_member in team_members],
		}
		return render(request, 'hackathontime_users/profile_slug.html', context)

	else:
		messages.warning(request, 'User doesn\'t exists.')
		return redirect('ht-home')

def hackathon_view(request, **kwargs):
	slug = kwargs['hackathon_slug']
	hackathon_object = Hackathon.objects.filter(hackathon_slug=slug)
	if hackathon_object:
		if request.method == "POST":
			if not request.user.profile.is_in_a_team:
				messages.warning(request, "You're not in a team. Either make one team or join one.")
				return redirect('ht-register-team')
			# print(dir(request.user))
			curr_team = request.user.profile.team
			curr_hackathon = hackathon_object[0]
			curr_hackathon.hackathon_team_going.add(curr_team)
			curr_hackathon.save()
			messages.success(request, f"Marked your team '{curr_team.team_name}' as going.")
			# return render(request, 'hackathontime_users/hackathon_slug.html', context)

		hackathon_object = hackathon_object[0]
		context={
			'hackathon': hackathon_object,
			'registered': hackathon_object.hackathon_team_going.filter(team_name=request.user.profile.team)
		}
		return render(request, 'hackathontime_users/hackathon_slug.html', context)
	else:
		messages.warning(request, 'Hackathon doesn\'t exists.')
		return redirect('ht-home')

def team_view(request, **kwargs):
	slug = kwargs['team_slug']
	
	context={

	}
	return render(request, 'hackathontime_users/team_slug.html', context)