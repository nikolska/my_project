from django.shortcuts import render
from django.http import HttpResponse

def images(request):
	return render(request, 'gallery/gallery.html')
