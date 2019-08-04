from .import views
from django.urls import path, re_path

app_name = 'universities'


urlpatterns = [
	re_path('^(?P<slug>[-\w]+)/$', views.university, name='university'),
	re_path('^(?P<slug>[\w-]+)/department/$', views.department, name='department'),
]