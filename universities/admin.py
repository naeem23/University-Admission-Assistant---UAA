from django.contrib import admin
from .models import *

# University Admin 
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]
    # prepopulated_fields = {'slug': ('name',)}

admin.site.register(University, UniversityAdmin)


# Department Admin
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['uni_name', 'dept_name']
	list_filter = ['uni_name', 'dept_name']

admin.site.register(Department, DepartmentAdmin)


# Unit Admin
class UnitAdmin(admin.ModelAdmin):
	list_display = ['uni_name', 'unit_name']
	list_filter = ['uni_name', 'unit_name']

admin.site.register(Unit, UnitAdmin)


# Faculty Admin
class FacultyAdmin(admin.ModelAdmin):
	list_display = ['uni_name', 'f_name']
	list_filter = ['uni_name', 'f_name']

admin.site.register(Faculty, FacultyAdmin)



# ----------------ApplySchedule admin-----------------
class ApplyScheduleAdmin(admin.ModelAdmin):
	list_display = ['uni_name', 'apply_start', 'apply_end']
	list_filter  = ['uni_name', 'apply_start', 'apply_end']

admin.site.register(ApplySchedule, ApplyScheduleAdmin)



# ---------------university rating-----------------
class RatingAdmin(admin.ModelAdmin):
	list_display = ['uni_name',]

admin.site.register(Rating, RatingAdmin)
		
		
