from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import Bloodbank,Donors
from .forms import BloodbankForm,DonorsForms



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
	form=BloodbankForm()

	return render(request, 'bloodbank.html',{'items': item,'form':form})


def faq(request):
	return render(request, 'faq.html')

def login(request):
	return render(request, 'login.html')

def add(request):	
	return render(request, 'add.html')

def donors(request):
	data=Donors.objects.all()
	return render(request, 'donorlist.html', {'data':data})


def register(request):	
	data=Donors.objects.all()
	if request.method == 'POST':
		form=DonorsForms(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponse('Thank You')
	else:
		form=DonorsForms()



	return render(request, 'registration.html', {'form':form,'data':data})



	
def events(request):	
	return render(request, 'events.html')
