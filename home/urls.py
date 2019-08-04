from django.urls import path, re_path
from .import views
app_name = 'home'


urlpatterns = [
	path('', views.home_page, name='homepage'),
	path('search/', views.search_view, name='search'),
	re_path('^(?P<category>\w+)-university/$', views.universityCategory, name='university_category'),
]