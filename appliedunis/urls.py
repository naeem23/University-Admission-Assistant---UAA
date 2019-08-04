from .import views
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

app_name = 'appliedunis'


urlpatterns = [
	path('api/cancel', login_required(views.cancelApi), name='delete_api'),
	path('api/apply/',  login_required(views.applyApi), name='api_uni'),
	path('api/read/',  login_required(views.markAsRead), name='read'),
]
