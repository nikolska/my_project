from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Photo


def images(request):
	categories = Category.objects.order_by('category')
	photos = Photo.objects.all()
	ctx = {
		'categories': categories,
		'photos': photos
	}
	return render(request, 'gallery/gallery.html', ctx)
