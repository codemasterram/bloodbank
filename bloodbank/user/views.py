from django.shortcuts import render,redirect
from user.models import Bloodbank



def index(request):
	return render(request, 'index.html')

def entry(request):
	return render(request, 'entry.html')



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