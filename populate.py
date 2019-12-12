from django.contrib.auth.models import User
from hackathontime_users.models import Team, Profile
from hackathontime_main.models import Hackathon
import random
import string

alpha_numeric = string.ascii_lowercase + string.ascii_uppercase + string.digits

for x in range(50):
    passs = ''.join(random.choices(alpha_numeric, k=3))
    u = User.objects.create_user(username=passs + ''.join(random.choices(alpha_numeric, k=5)),
                                 first_name=''.join(random.choices(alpha_numeric, k=10)),
                                 last_name=''.join(random.choices(alpha_numeric, k=5)),
                                 email=''.join(random.choices(alpha_numeric, k=10))+"@abcd.com", password=passs)
    u.profile.gender = random.choice("MFO")
    u.profile.bio = ''.join(
        [''.join(random.choices(alpha_numeric, k=20)) for _ in range(10)])
    u.profile.college = str(random.randint(1, 200))
    try:
        u.save()
    except:
        pass

    with open('users_made.txt', "a") as f:
        f.write(u.username+"\n")

print("Done creating 50 users")
