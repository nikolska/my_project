from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product

def products(request):
	product = Product.objects.all()
	return render(request, 'services/services.html', {'product_list':product})
