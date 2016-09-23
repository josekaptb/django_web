# url de inici
from django.conf.urls import include,url
from .import views

urlpatterns = [
	url(r'^$',views.pag_inicial),
	url(r'^inici/$',views.pag_inicial),
]