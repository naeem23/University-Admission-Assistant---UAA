from .import views
from appliedunis.views import application, notifications
from contact.views import messages
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from interestedunis.views import interestedUnis
from . import views
app_name = 'accounts'


urlpatterns = [
	path('signup/', views.signup_views, name='signup'),
    path('login/', views.login_views, name='login'),
	path('logout/', views.logout_views, name='logout'),

	path('registration-first-step/', login_required(views.registrationFirst), name='registration_first'),
	path('registration-second-step/', login_required(views.registrationSecond), name='registration_second'),
    path('registration-third-step/', login_required(views.registrationThird), name='registration_third'),

    re_path('^(?P<username>\w+)/$', login_required(views.profile), name='profile'),
    re_path('^(?P<username>\w+)/messages/$', login_required(messages), name='messages'),
    re_path('^(?P<username>\w+)/eligible-universities/$', login_required(views.eligible_list), name='eligible_list'),
    re_path('^(?P<username>\w+)/application/$', login_required(application), name='application'),
    re_path('^(?P<username>\w+)/interested-universities/$', login_required(interestedUnis), name='interested_unis'),
    re_path('^(?P<username>\w+)/notifications/$', login_required(notifications), name='notifications'),

    re_path('^(?P<username>\w+)/edit-basic-info/$', login_required(views.editBasicInfo), name='edit_basic'),
    re_path('^(?P<username>\w+)/edit-ssc-info/$', login_required(views.editSscInfo), name='edit_ssc'),
    re_path('^(?P<username>\w+)/edit-hsc-info/$', login_required(views.editHscInfo), name='edit_hsc'),
]
