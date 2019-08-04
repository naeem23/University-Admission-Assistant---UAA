from .import views
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

app_name = 'interestedunis'


urlpatterns = [
	path('api/remove', login_required(views.ApiRemoveInterested), name='remove_interested'),
	path('api/add/', login_required(views.AddInterestedApi), name='api_add'),
]
