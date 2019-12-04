from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm , ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
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
		user_form = UserForm()
		# profile_form = ProfileForm()

	return render(request, 'hackathontime_users/register.html', {'user_form':user_form}) #, 'profile_form':profile_form})

@login_required
def profile(request):
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			# image check
			curr_image = Image.open(profile_form.cleaned_data.get('image'))
			if curr_image.height < 400 or curr_image.width < 400:
				messages.warning(request, 'Image must be larger than 400x400 pixels.')
				return redirect('ht-profile')
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

	context = {
		'user_form' : user_form,
		'profile_form' : profile_form
	}

	return render(request, 'hackathontime_users/profile.html', context)