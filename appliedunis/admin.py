from django.contrib import admin
from .models import *

admin.site.register(ApplyApplication)

class NotificationAdmin(admin.ModelAdmin):
	list_display = ['receiver', 'message', 'is_read']

admin.site.register(Notification, NotificationAdmin)
