from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'user', 'message']

admin.site.register(Contact, ContactAdmin)

