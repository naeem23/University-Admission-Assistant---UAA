from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'ssc_roll', 'ssc_reg', 'hsc_roll', 'hsc_reg']
    list_filter = ['user',]

admin.site.register(UserProfile, UserProfileAdmin)

