from .import views
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
app_name = 'feedback'


urlpatterns = [
	path('', login_required(views.sendFeedback), name='send_feedback'),
]