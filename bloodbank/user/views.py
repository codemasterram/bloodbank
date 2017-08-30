from django.shortcuts import render



def index(request):
	return render(request, 'index.html')



def bloodstock(request):
	return render(request, 'bloodstock.html')


def bloodbank(request):
	return render(request, 'bloodbank.html')


def faq(request):
	return render(request, 'faq.html')

def login(request):
	return render(request, 'login.html')

def donorlist(request):
	return render(request, 'donorlist.html')