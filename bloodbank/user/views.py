from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import Bloodbank
from .forms import BloodbankForm



def index(request):
	return render(request, 'index.html')

def entry(request):
	data=Bloodbank.objects.all()
	if request.method == 'POST':
		form=BloodbankForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponse('Thank You')
	else:
		form=BloodbankForm()



	return render(request, 'entry.html', {'form':form,'data':data})



def bloodstock(request):
	item = Bloodbank.objects.all()
	return render(request, 'bloodstock.html',{'items': item})


def bloodbank(request):
	item = Bloodbank.objects.all()

	return render(request, 'bloodbank.html',{'items': item})


def faq(request):
	return render(request, 'faq.html')

def login(request):
	return render(request, 'login.html')

def add(request):	
	return render(request, 'add.html')

def donors(request):	
	return render(request, 'donorlist.html')

def register(request):	
	return render(request, 'registration.html')
def events(request):	
	return render(request, 'events.html')
