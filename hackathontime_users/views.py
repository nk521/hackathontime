from django.shortcuts import render, redirect
from django.contrib import messages # , CreatePostForm
from .forms import UserForm, ProfileUpdateForm, CreateTeamForm, TeamOverviewForm
from django.contrib.auth.decorators import login_required
from .models import Team, Profile  # , Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from PIL import Image
from hackathontime_main.models import Hackathon

# /register
def register(request):
    if request.user.is_authenticated:
        return redirect('ht-home')

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            #save form
            user = user_form.save()
            user.profile.is_active = False
            gender = user_form.cleaned_data.get('gender')
            user.profile.gender = gender
            user.profile.save()
            # account activation mail
            current_site = get_current_site(request)
            mail_subject = 'Activate your HackathonTime account.'
            message = render_to_string('hackathontime_users/activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            # login to new account. and throw some messages.
            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Account for username \"{username}\" has been created.")
            messages.warning(request, "Please confirm your E-mail address.")
            new_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('ht-home')
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        user_form = UserForm()

    context = {
        'title': 'Register',
        'user_form': user_form,
    }

    return render(request, 'hackathontime_users/register.html', context)

# /register/activate
def activate(request, uidb64, token):
    # check for uid
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # grant access to user
        user.profile.is_active = True
        user.profile.save()
        messages.success(request, 'Thank you for your email confirmation.')
        return redirect('ht-profile')
    else:
        messages.warning(request, 'Activation link is invalid.')
        return redirect('ht-profile')

# /profile
@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            # image check
            curr_image = Image.open(profile_form.cleaned_data.get('image'))
            if curr_image.height < 295 or curr_image.width < 295:
                messages.warning(
                    request, 'Image must be larger than 300x300 pixels.')
                curr_image.close()
                return redirect('ht-profile')

            # save form
            profile_form.save()
            curr_image.close()
            messages.success(request, f"Account successfully updated for {request.user.username}'s profile!")
            return redirect('ht-profile')
        else:
            messages.warning(request, 'Please correct the errors below.')
            return redirect('ht-profile')

    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        team_members = Profile.objects.filter(team=request.user.profile.team)

    context = {
        'title': 'Profile',
        'profile_form': profile_form,
        'team_members': team_members,
    }

    return render(request, 'hackathontime_users/profile.html', context)


@login_required
def register_team(request):
    if not request.user.profile.is_active:
        messages.warning(request, "Please confirm your E-mail address.")
        return redirect('ht-profile')

    if request.user.profile.is_in_a_team:
        messages.warning(request, "You're already in a team.")
        return redirect('ht-profile')

    if request.method == "POST":
        team_form = CreateTeamForm(request.POST)

        if team_form.is_valid():
            team_instance = team_form.save()
            profile = request.user.profile
            profile.team = team_instance
            profile.is_in_a_team = True
            profile.save()
            # request.user.profile.team = team_form
            # request.user.profile.save()
            team_name = team_form.cleaned_data.get('team_name')
            messages.success(request, f"Team '{team_name}' successfully created!")
            return redirect('ht-profile')
        else:
            messages.warning(request, 'This name is already taken.')
            return redirect('ht-profile')
    else:
        team_form = CreateTeamForm()

    context = {
        'title': 'Register Team',
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

        context = {
            'title': f'{profile_object.user.username}\'s profile',
            'profile': profile_object,
            'team_members': [str(team_member) for team_member in team_members],
        }
        return render(request, 'hackathontime_users/profile_slug.html', context)

    else:
        messages.warning(request, 'User doesn\'t exists.')
        return redirect('ht-home')


@login_required
def hackathon_view(request, **kwargs):
    slug = kwargs['hackathon_slug']
    hackathon_object = Hackathon.objects.filter(hackathon_slug=slug)
    if hackathon_object:
        if request.method == "POST":

            if not request.user.profile.is_active:
                messages.warning(
                    request, "Please confirm your E-mail address.")
                return redirect('ht-profile')

            if not request.user.profile.is_in_a_team:
                messages.warning(
                    request, "You're not in a team. Either make one team or join one.")
                return redirect('ht-register-team')
            curr_team = request.user.profile.team
            curr_hackathon = hackathon_object[0]
            curr_hackathon.hackathon_team_going.add(curr_team)
            curr_hackathon.save()
            messages.success(request, f"Marked your team '{curr_team.team_name}' as going.")

        hackathon_object = hackathon_object[0]
        context = {
            'title': f'{hackathon_object.hackathon_name}',
            'hackathon': hackathon_object,
            'registered': hackathon_object.hackathon_team_going.filter(team_name=request.user.profile.team)
        }
        if hackathon_object.hackathon_past:
            context['winner'] = hackathon_object.hackathon_won
            context['runnerup1'] = hackathon_object.hackathon_runnerup_1
            context['runnerup2'] = hackathon_object.hackathon_runnerup_2

        return render(request, 'hackathontime_users/hackathon_slug.html', context)
    else:
        messages.warning(request, 'Hackathon doesn\'t exists.')
        return redirect('ht-home')


@login_required
def team(request):
    profile = request.user.profile
    if not profile.is_in_a_team:
        messages.warning(
            request, 'You\'re not in team. Either create one or join one.')
        return redirect('ht-register-team')

    if request.method == "POST":
        team_overview_form = TeamOverviewForm(request.POST)

        if team_overview_form.is_valid():
            team_overview = team_overview_form.cleaned_data.get(
                'team_overview')
            profile.team.team_overview = team_overview
            profile.team.save()

        else:
            messages.warning(request, 'Please correct the errors below.')
            return redirect('ht-team')

    else:
        team_overview_form = TeamOverviewForm(
            instance=request.user.profile.team)

    # this code is for team blog.
    # if request.method == "POST":
    #     post_form = CreatePostForm(request.POST)

    #     if post_form.is_valid():
    #         post_instance = post_form.save()
    #         post_instance.author = profile.team
    #         post_instance.save()

    #     else:
    #         messages.warning(request, 'Please correct the errors below.')
    #         return redirect('ht-team')

    # else:
    #     post_form = CreatePostForm()

    team_members = Profile.objects.filter(team=profile.team)
    hackathons = Hackathon.objects.filter(
        hackathon_team_going=profile.team)
    won_hackathons = Hackathon.objects.filter(
        hackathon_won=profile.team)

    context = {
        'title': 'Your Team',
        'team_members': team_members,
        'hackathons': hackathons,
        'won_hackathons': won_hackathons,
        'form': team_overview_form,
        # 'form': post_form,
        # 'posts': Post.objects.filter(author = profile.team),
    }

    return render(request, 'hackathontime_users/team.html', context)


@login_required
def team_view(request, **kwargs):
    slug = kwargs['team_slug']

    if request.user.profile.is_in_a_team:
        if request.user.profile.team.team_slug == slug:
            return redirect('ht-team')

    team_object = Team.objects.filter(team_slug=slug)
    if team_object:
        team_object = team_object[0]
        team_members = Profile.objects.filter(team=team_object)
        hackathons = Hackathon.objects.filter(
            hackathon_team_going=team_object)
        won_hackathons = Hackathon.objects.filter(
            hackathon_won=team_object)

        context = {
            'title': f'{team_object.team_name} Team',
            'team_name': team_object.team_name,
            'team_overview': team_object.team_overview,
            'team_members': team_members,
            'hackathons': hackathons,
            'won_hackathons': won_hackathons,
            # 'posts': Post.objects.filter(author__team_slug = slug),
        }
        return render(request, 'hackathontime_users/team_slug.html', context)

    else:
        messages.warning(request, 'Team doesn\'t exists.')
        return redirect('ht-home')


@login_required
def team_join(request, **kwargs):
    if not request.user.profile.is_active:
        messages.warning(request, "Please confirm your E-mail address.")
        return redirect('ht-profile')

    code = kwargs['code']
    team_object = Team.objects.filter(team_code=code)
    if not team_object:
        messages.warning(request, 'Code is invalid.')
        return redirect('ht-home')

    team_object = team_object[0]
    profile = request.user.profile
    if profile.is_in_a_team:
        messages.warning(request, 'You\'re already in a team.')
        return redirect('ht-home')

    profile.team = team_object
    profile.is_in_a_team = True
    profile.save()

    messages.success(request, f'You successfully joined \'{team_object.team_name}\' team.')
    return redirect('ht-profile')
