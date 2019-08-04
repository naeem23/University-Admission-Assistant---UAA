from .import views
from django.urls import path, re_path
app_name = 'contact'


urlpatterns = [
	path('', views.contactUs, name='contact_us'),
]