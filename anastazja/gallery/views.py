from django.shortcuts import render
from django.http import HttpResponse

def images(request):
	return HttpResponse('<h1>GALLERY</h1>')
