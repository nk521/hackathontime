from django.shortcuts import render
from hackathontime_users.models import Profile, Team
from hackathontime_main.models import Hackathon
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# create a view for blogs. paginate that and make a submission form for blog itself.