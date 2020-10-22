from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
	path('', views.search, name='contacts-search'),
]