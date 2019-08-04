from .forms import *
from .models import UserProfile
from appliedunis.models import *
from universities.models import Unit
from interestedunis.models import InterestedUni
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from django.contrib.auth import views as auth_views



# --------------------------------------
# ------------Signup Views--------------
# --------------------------------------
def signup_views(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			user = form.signup(request)
			user.save()
			return redirect('accounts:login')

	else:
		form = SignupForm()

	context = {
		'form': form,
	}

	return render(request, 'accounts/signup.html', context)




# --------------------------------------
# ------------Login Views--------------
# --------------------------------------
def login_views(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = form.login(request)
			if user:
				login(request,user)       
				return redirect('home:homepage')
	else:
		form = LoginForm()

	context = {
		'form': form,
	}

	return render(request, 'accounts/login.html', context)




# --------------------------------------
# ------------Logout Views--------------
# --------------------------------------
def logout_views(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home:homepage')




# --------------------------------------
# ---------Registration Views-----------
# --------------------------------------
def registrationFirst(request):
	instance = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		form = BasicInformation(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('accounts:registration_second')
	else:
		form = BasicInformation(instance=instance)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_first.html', context)


# -----------------------------------------
# ---------Edit Basic Info Views-----------
# -----------------------------------------
def editBasicInfo(request, username):
	instance = get_object_or_404(UserProfile, user=request.user)
	
	form = BasicInformation(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
			form.save()
			return redirect('accounts:profile', request.user)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_first.html', context)


# --------------------------------------
# ---------Registration Views-----------
# --------------------------------------
def registrationSecond(request):
	instance = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		form = SscInformation(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('accounts:registration_third')
	else:
		form = SscInformation(instance=instance)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_second.html', context)


# -----------------------------------------
# ---------Edit Basic Info Views-----------
# -----------------------------------------
def editSscInfo(request, username):
	instance = get_object_or_404(UserProfile, user=request.user)
	
	form = SscInformation(request.POST or None, instance=instance)
	if form.is_valid():
			form.save()
			return redirect('accounts:profile', request.user)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_second.html', context)


# --------------------------------------
# ---------Registration Views-----------
# --------------------------------------
def registrationThird(request):
	instance = get_object_or_404(UserProfile, user=request.user)
	if request.method == 'POST':
		form = HscInformation(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('accounts:profile', request.user)
	else:
		form = HscInformation(instance=instance)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_third.html', context)


# -----------------------------------------
# ---------Edit Basic Info Views-----------
# -----------------------------------------
def editHscInfo(request, username):
	instance = get_object_or_404(UserProfile, user=request.user)
	
	form = HscInformation(request.POST or None, instance=instance)
	if form.is_valid():
			form.save()
			return redirect('accounts:profile', request.user)

	context = {
		'form': form,
	}

	return render(request, 'accounts/registration_third.html', context)



# --------------------------------------
# --------Student Profile Views---------
# --------------------------------------
def profile(request, username):
	user = get_object_or_404(User, username=username)
	userprofile = UserProfile.objects.get(user=user)
	unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()

	context = {
		'user': user,
		'userprofile': userprofile,
		'count': unread_notification,
	}

	return render(request, 'accounts/profile.html', context)



# ------------------------------------------
# ---------- Eligible List view ------------
# ------------------------------------------
def eligible_list(request, username):
	userprofile = UserProfile.objects.get(user=request.user)
	interested_unis = InterestedUni.objects.get(user=request.user)
	applied_unit = ApplyApplication.objects.filter(user=request.user)

	ssc_year = userprofile.ssc_pass_y
	hsc_year = userprofile.hsc_pass_y

	applicant_group = userprofile.hsc_group

	ssc_gpa = userprofile.ssc_gpa
	hsc_gpa	= userprofile.hsc_gpa
	total_gpa = ssc_gpa + hsc_gpa

	physics = userprofile.physics
	chemistry = userprofile.chemistry
	math = userprofile.math
	biology = userprofile.biology
	english = userprofile.english
	bangla = userprofile.bangla

	units = Unit.objects.all().order_by('uni_name')
	unit_list = []

	if applicant_group == 'science':
		for unit in units:
			sub_total = physics+chemistry+math			 	
			if unit.bio_gpa > 1.00:
				sub_total += biology
			if unit.en_gpa > 1.00:
				sub_total += english
			if unit.ban_gpa > 1.00:
				sub_total += bangla

			if ssc_year in unit.ssc_year and hsc_year in unit.hsc_year and unit.science and ssc_gpa >= unit.science_gpa and hsc_gpa >= unit.science_gpa and total_gpa >= unit.science_tgpa:
				if physics >= unit.phy_gpa and chemistry >= unit.chem_gpa and math >= unit.math_gpa and biology >= unit.bio_gpa and english >= unit.en_gpa and bangla >= unit.ban_gpa and sub_total >= unit.tgpa:
					unit_list.append(unit)
	

	if applicant_group == 'commerce':
		for unit in units:
			if ssc_year in unit.ssc_year and hsc_year in unit.hsc_year and unit.commerce and ssc_gpa >= unit.commerce_gpa and hsc_gpa >= unit.commerce_gpa and total_gpa >= unit.commerce_tgpa:
			 	unit_list.append(unit)


	if applicant_group == 'humanities':
		for unit in units:
			if ssc_year in unit.ssc_year and hsc_year in unit.hsc_year and unit.humanities and ssc_gpa >= unit.arts_gpa and hsc_gpa >= unit.arts_gpa and total_gpa >= unit.arts_tgpa:
			 	unit_list.append(unit)

	
	# following line of is used to check whether a unit is in applied_units
	status_list = []
	applied_units = []

	for a in applied_unit:
		applied_units.append(a.unit.id)

	for u in unit_list:
		if u.id in applied_units:
			status = 'yes'
		else:
			status = 'no'
		status_list.append(status)
	# end of the section

	newlist = list(zip(unit_list, status_list))
	
	# paginator
	page = request.GET.get('page', 1)
	paginator = Paginator(newlist, 5)
	try:
		units = paginator.page(page)
	except PageNotAnInteger:
		units = paginator.page(5)
	except EmptyPage:
		units = paginator.page(paginator.num_pages)

	# Notification count
	unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()
	context = {
		'userprofile': userprofile,
		'units': units,
		'applied_unit': applied_unit,
		'interested_unis': interested_unis,
		'count': unread_notification
	}

	return render(request, 'accounts/eligible_list.html', context)




class PasswordReset(auth_views.PasswordResetView):
	template_name = 'accounts/password_reset.html'
	html_email_template_name = 'accounts/password_reset_email.html'
	from_email = 'admin@uaa.com'

class PasswordResetDone(auth_views.PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'
