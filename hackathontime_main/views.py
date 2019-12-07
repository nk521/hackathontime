from django.shortcuts import render
from django.http import HttpResponse
from .models import Hackathon
from datetime import datetime, timedelta, timezone
import pytz

def check_hackathon_time():
	future_and_ongoing_hackathons = [Hackathon.objects.filter(hackathon_future=True), Hackathon.objects.filter(hackathon_ongoing=True)]
	for hackathons in future_and_ongoing_hackathons:
		for hackathon_object in hackathons:
			hackathon_date = hackathon_object.hackathon_date.astimezone(pytz.timezone("Asia/Kolkata"))
			hackathon_date_plus_duration = hackathon_date + timedelta(hours=hackathon_object.hackathon_period)
			now = datetime.now().astimezone(pytz.timezone('Asia/Kolkata'))
			# print(hackathon_object.hackathon_name, hackathon_date, hackathon_date_plus_duration)
			if now < hackathon_date:
				hackathon_object.hackathon_past = False
				hackathon_object.hackathon_ongoing = False
				hackathon_object.hackathon_future = True

			elif hackathon_date <= now <= hackathon_date_plus_duration:
				hackathon_object.hackathon_past = False
				hackathon_object.hackathon_ongoing = True
				hackathon_object.hackathon_future = False

			else:
				hackathon_object.hackathon_past = True
				hackathon_object.hackathon_ongoing = False
				hackathon_object.hackathon_future = False
			hackathon_object.save()



#count Hackahton.objects.count
def home(request):
	check_hackathon_time()
	future_hackathons = Hackathon.objects.filter(hackathon_future=True)
	# past_hackathons = Hackathon.objects.filter(hackathon_past=True)
	on_going_hackathons = Hackathon.objects.filter(hackathon_ongoing=True)
	context = {
		'future_hackathons': future_hackathons.order_by('hackathon_date')[0:3],
		# 'past_hackathons': Hackathon.objects.filter(hackathon_past=True).order_by('hackathon_date')[0:3],
		'on_going_hackathons': on_going_hackathons.order_by('hackathon_date')[0:3],
		'on_going_count': on_going_hackathons.count(),
		'future_count': future_hackathons.count(),
	}
	return render(request, 'hackathontime_main/home.html', context)

# def about(request):
# 	return HttpResponse("<h1>about</h1>")
