import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from deals.models import Deal, DealForm

def home(request):
	today_datetime = datetime.datetime.now()
	year = today_datetime.year
	month = today_datetime.month
	if (month >= 1) and (month <=9):
		month = '0' + str(month)
	day = today_datetime.day
	if (day>=1) and (day<=9):
		day ='0' + str(day)
	today = str(year) + '-' + str(month) + '-' + str(day)

	deals = Deal.objects.filter(date=today)
	return render_to_response("home.html", {'request': request, 'deals': deals, 'today_datetime': today_datetime}, context_instance=RequestContext(request))
	
def about_us(request):
	pass

def contact_us(request):
	pass
