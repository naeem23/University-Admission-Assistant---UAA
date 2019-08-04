from django.contrib import admin
from .models import Feedback


# Feedback admin
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'email']

admin.site.register(Feedback, FeedbackAdmin)
