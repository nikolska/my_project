from django.shortcuts import render
from django.http import HttpResponse

def products(request):
	return HttpResponse('<h1>SERVICES</h1>')
