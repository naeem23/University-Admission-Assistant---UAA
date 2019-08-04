from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from feedback.models import Feedback
from universities.models import *

# -----------------------------------
# ---------- Home Page View ---------
# -----------------------------------
def home_page(request):
	feedbacks = Feedback.objects.all().order_by('-send_date')[:3]

	# calculation for remaining deadline time
	units = Unit.objects.all()
	apply_deadline = []
	apply_units = []
	exam_deadline = []
	exam_units = []
	now = datetime.now(timezone.utc)

	for u in units:
		deadline = u.apply_dead
		diff = relativedelta(deadline, now)
		if diff.months == 0 and diff.days <= 7 and diff.days >= 0 and diff.hours >= 0 and diff.minutes >= 0:
			full_format = str(diff.days)+" Days "+str(diff.hours)+" Hours "+str(diff.minutes)+" Minutes"
			apply_deadline.append(full_format)
			apply_units.append(u)


	for u in units:
		exam_dead = u.exam_date
		remain = relativedelta(exam_dead, now)
		if remain.months == 0 and remain.days <= 7 and remain.days >= 0 and remain.hours >= 0 and remain.minutes >= 0:
			formate = str(remain.days)+" Days "+str(remain.hours)+" Hours "+str(remain.minutes)+" Minutes"
			exam_deadline.append(formate)
			exam_units.append(u)

	deadline_list = zip(apply_units, apply_deadline)
	exam_deadlist = zip(exam_units, exam_deadline)
	# calculation remaining time ends here

	context = {
		'deadlines': deadline_list,
		'examdead': exam_deadlist,
		'feedbacks': feedbacks
	}
	return render(request, 'home/index.html', context)


# --------------------------------------
# ------ University Category View ------
# --------------------------------------
def universityCategory(request, category):
	if category == 'agricultural':
		category = 'agricultural'
	elif category == 'engineering':
		category = 'engineering'
	elif category == 'medical':
		category = 'medical'
	elif category == 'general':
		category = 'general'
	elif category == 'science':
		category = 'science'

	university = University.objects.filter(category=category)

	context = {
		'university': university,
		'category': category
	}
	return render(request, 'home/university_category.html', context)



# -------------------------------------------
# --------- Search University View ----------
# -------------------------------------------
def search_view(request):
	queryset_list = University.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(name__icontains=query) |
			Q(category__icontains=query) |
			Q(about__icontains=query)
		).distinct()

	context = {
		'universities': queryset_list,
	}

	return render(request, 'home/search_result.html', context)