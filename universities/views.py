from django.shortcuts import render, get_object_or_404, redirect
from universities.models import *


# -----------------------------------------
# ------------ University View ------------
# -----------------------------------------
def university(request, slug):
	university = get_object_or_404(University, slug=slug)
	units = Unit.objects.filter(uni_name=university)
	faculties = Faculty.objects.filter(uni_name=university).order_by('f_name')
	departments = Department.objects.filter(uni_name=university).order_by('dept_name')
	ratings = Rating.objects.get(uni_name=university)
	dates = ApplySchedule.objects.get(uni_name=university)
	
	context = {
		'uni': university,
		'units': units,
		'faculties': faculties,
		'departments': departments,
		'ratings': ratings,
		'dates': dates
	}

	return render(request, 'universities/uni.html', context)



# -----------------------------------------
# ------------ Department View ------------
# -----------------------------------------
def department(request, slug):
	department = get_object_or_404(Department, slug=slug)

	context = {
		'dept': department,
	}

	return render(request, 'universities/dept.html', context)


	