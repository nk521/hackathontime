from django.db import models
from hackathontime_users.models import Profile, Team
from hackathontime_main.models import Hackathon
from django.contrib.auth.models import User

# add blog model, foreign key to hackathontime_users.models.Team