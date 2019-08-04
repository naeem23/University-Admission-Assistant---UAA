from .import views
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
app_name = 'staff'


urlpatterns = [
	# apply request list and delete url
	path('', login_required(views.staff_home), name='staff_home'),
	path('api/delete-apply-request/', login_required(views.ApiDeleteApplyRequest), name='delete_request'),


	# university list add and delete url
	path('universities/', login_required(views.universities), name='universities'),
	path('add-university/', login_required(views.add_university), name='add_university'),
	path('api/delete-university/', login_required(views.ApiDeleteUniversity), name='delete_uni'),


	# faculty delete url
	path('api/delete-faculty/', login_required(views.ApiDeleteFaculty), name='delete_faculty'),


	# department list, add and delete url
	path('departments/', login_required(views.departments), name='departments'),
	path('api/delete-department/', login_required(views.ApiDeleteDepartment), name='delete_department'),


	# unit list and delete url
	path('units/', login_required(views.units), name='units'),
	path('api/delete-unit/', login_required(views.ApiDeleteUnit), name='delete_unit'),


	# feedback list url
	path('feedbacks/', login_required(views.feedbacks), name='feedbacks'),
	path('api/delete-feedback/', login_required(views.ApiDeleteFeedback), name='delete_feedback'),
	path('api/approve-feedback/', login_required(views.ApiApproveFeedback), name='approve_feedback'),


	# contact messages url
	path('students-queries/', login_required(views.queries), name='queries'),
	path('api/replied-message/', login_required(views.ApiRepliedMessage), name='replied_message'),
	re_path('reply-message/(?P<id>\d+)/$', login_required(views.replyMessage), name='msg_reply'),

	# sending mail to all intereseduni user 
	path('send-mail/', login_required(views.sendMail), name='send_mail'),

	# edit university, add rating and add apply schedule url
	re_path('^edit-university/(?P<id>\d+)/$', login_required(views.edit_university), name='edit_university'),
	re_path('^add-university-rating/(?P<obj_id>[0-9]+)/$', login_required(views.uni_rating), name='uni_rating'),
	re_path('^add-apply-schedule/(?P<schedule_id>[0-9]+)/$', login_required(views.apply_schedule), name='apply_schedule'),
	

	# edit apply request url
	re_path('^edit-apply-request/(?P<id>\d+)/$', login_required(views.editRequest), name='edit_request'),


	# department url
	re_path('add-department/(?P<id>\d+)/$', login_required(views.addDepartment), name='add_department'),
	re_path('^edit-department/(?P<id>\d+)/$', login_required(views.edit_department), name='edit_department'),


	# faculty url
	re_path('add-faculty/(?P<uni_id>\d+)/$', login_required(views.addFaculty), name='add_faculty'),
	re_path('edit-faculty/(?P<id>\d+)/$', login_required(views.edit_faculty), name='edit_faculty'),


	# add and edit unit url
	re_path('^university/(?P<id>\d+)/add-unit/$', login_required(views.addUnit), name='add_unit'),
	re_path('^edit-unit/(?P<id>\d+)/$', login_required(views.editUnit), name='edit_unit'),
]