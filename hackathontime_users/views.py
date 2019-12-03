from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm #, ProfileForm

def register(request):
	if request.method == "POST":
		user_form = UserForm(request.POST)
		# profile_form = ProfileForm(request.POST)

		if user_form.is_valid(): #and profile_form.is_valid():
			user_form.save()
			# profile_form.save()
			username = user_form.cleaned_data.get('username')
			messages.success(request, f"Successfully created an account for {username}!")
			return redirect('ht-home')
		else:
			messages.warning(request, 'Please correct the error below.')
	else:
		user_form = UserForm()
		# profile_form = ProfileForm()

	return render(request, 'hackathontime_users/register.html', {'user_form':user_form}) #, 'profile_form':profile_form})