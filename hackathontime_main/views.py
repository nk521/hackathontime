from django.shortcuts import render
from django.http import HttpResponse
from .models import Hackathon

def check_hackathon_time(hackathon_date):
	# if 
	pass

#count Hackahton.objects.count
def home(request):
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
