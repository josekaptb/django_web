# url de empresa
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.contacta),
	url(r'^contacta/$',views.contacta),
]