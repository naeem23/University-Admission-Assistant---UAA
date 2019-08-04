from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from appliedunis.models import *
from appliedunis.forms import ApplyApplicationForm
from contact.models import Contact
from contact.forms import ReplyMessage
from feedback.models import Feedback
from interestedunis.models import InterestedUni
from universities.forms import *
from universities.models import *
from django.core.mail import send_mail, send_mass_mail
from uaa.settings import EMAIL_HOST_USER
from datetime import datetime, timedelta, date

# ------------------------
# --home view for staff---
# ------------------------
def staff_home(request):
	if request.user.is_staff or request.user.is_superuser:
		application_list = ApplyApplication.objects.all().order_by('-creation_date')

		query = request.GET.get("q")
		if query:
			application_list = application_list.filter(
				Q(application_id__icontains=query) |
				Q(status__icontains=query) |
				Q(user__username__icontains=query)
			).distinct()

		# paginator
		page = request.GET.get('page', 1)
		paginator = Paginator(application_list, 3)
		try:
			applications = paginator.page(page)
		except PageNotAnInteger:
			applications = paginator.page(1)
		except EmptyPage:
			applications = paginator.page(paginator.num_pages)

		context = {
			'object': applications,
		}
		return render(request, 'staff/staff_home.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ---------------------------------------
# ------------Edit Requests--------------
# ---------------------------------------
def editRequest(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(ApplyApplication, id=id)
		
		form = ApplyApplicationForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.taken_by = str(request.user)
			instance.save()

			applicant = instance.user
			status = instance.status
			university = instance.unit.uni_name
			unit = instance.unit.unit_name
			admit_card = instance.admit_card

			if (status == 'accepted' or status == 'completed') and not instance.information:
				message = 'Your application request for '+str(university)+" Unit "+str(unit)+' is '+ str(status) + '.'
				Notification.objects.create(receiver=applicant, message=message)
			
			# Sending mail when application is processing
			if status == 'processing' and not instance.information:
				subject = 'University Admission Assistant'
				from_email = settings.EMAIL_HOST_USER
				to_email = [applicant.email]
				message = 'Your application request for ' +str(university)+' Unit '+str(unit)+' is processing. Shortly you will get a call from Rocekt for payment. If you are not interested to apply ignore the call.'

				send_mail(
					subject = subject,
					from_email = from_email,
					recipient_list = to_email,
					message = message,
				    fail_silently=False,
				)

			if instance.information:
				message = 'You have a update for '+str(university)+" Unit "+str(unit)+'.'
				Notification.objects.create(receiver=applicant, message=message)

			if admit_card:
				message = str(university)+' Unit '+str(unit)+' admit card is available to download.'
				Notification.objects.create(receiver=applicant, message=message)
				
			return redirect('staff:staff_home')

		context = {
			'form': form,
		}
		return render(request, 'staff/edit_request.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ----------------------------------------
# ---------Apply Request delete view------
# ----------------------------------------
def ApiDeleteApplyRequest(request):
	if request.user.is_staff or request.user.is_superuser:
		if request.user.is_staff:
			if request.GET.get('obj_id'):
				request_id = request.GET.get('obj_id')
				request_obj = ApplyApplication.objects.get(id=request_id)

				data = dict()
				if request_obj in ApplyApplication.objects.all():
					request_obj.delete()
					data['delete'] = 'success'

					requests = ApplyApplication.objects.all()

					# paginator
					page = request.GET.get('page', 1)
					paginator = Paginator(requests, 3)
					try:
						applications = paginator.page(page)
					except PageNotAnInteger:
						applications = paginator.page(1)
					except EmptyPage:
						applications = paginator.page(paginator.num_pages)


					data['html_requests'] = render_to_string(
							'staff/apply_requests.html', {'object': applications}
						)

				return JsonResponse(data)

		return JsonResponse({
				'delete': 'error'
			})
	
	else:
		return render(request, 'staff/page_not_found.html')




# ---------------------------------------
# --Applications Requests--
# ---------------------------------------
def universities(request):
	if request.user.is_staff or request.user.is_superuser:
		university_list = University.objects.all()

		# paginator
		page = request.GET.get('page', 1)
		paginator = Paginator(university_list, 5)
		try:
			university = paginator.page(page)
		except PageNotAnInteger:
			university = paginator.page(1)
		except EmptyPage:
			university = paginator.page(paginator.num_pages)

		context = {
			'object': university,
		}

		return render(request, 'staff/universities.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ----------------------------------
# --add university view for staff---
# ----------------------------------
def add_university(request):
	if request.user.is_staff or request.user.is_superuser:
		if request.method == 'POST':
			form = UniBasicAddForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				instance = form.save()

				# get university object id and object
				uni_id = instance.id
				uni_obj = University.objects.get(id=uni_id)

				# creating rated university object and get id for redirecting
				rating = Rating.objects.create(uni_name=uni_obj)
				schedule = ApplySchedule.objects.create(uni_name=uni_obj)
				# url = '/staff/add-university-rating/' + str(obj_id) + '/'
				# return HttpResponseRedirect(url)
				return redirect('staff:universities')
		else:
			form = UniBasicAddForm()

		context ={
			'form': form,
		}
		return render(request, 'staff/add_university.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ----------------------------------
# --add university rating view -----
# ----------------------------------
def edit_university(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(University, id=id)
		
		form = UniBasicAddForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()

			# get university object id and object
			# uni_id = instance.id
			# uni_obj = University.objects.get(id=uni_id)

			# # creating rated university object and get id for redirecting
			# rated_uni = Rating.objects.get(uni_name=uni_obj)
			# obj_id = rated_uni.id
			# return redirect('staff:uni_rating', obj_id=obj_id)
			return redirect('staff:universities')

		context = {
			'form': form,
		}
		return render(request, 'staff/add_university.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')




# ----------------------------------
# --add university rating view -----
# ----------------------------------
def uni_rating(request, obj_id):
	if request.user.is_staff or request.user.is_superuser:
		university = University.objects.get(id=obj_id)
		instance = get_object_or_404(Rating, uni_name=university)

		# form to add rating for university
		form = UniRatingForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()

			# get university object id and object
			# obj = instance.id
			# rated_obj = Rating.objects.get(id=obj)
			# name = rated_obj.uni_name

			# creating rated university object and get id for redirecting
			# object, created = ApplySchedule.objects.get_or_create(uni_name=name)
			# obj_id = object.id
			# print(obj_id)
			# return redirect('staff:apply_schedule', schedule_id=obj_id)
			return redirect('staff:universities')

		context = {
			'form': form,
			'instance': instance,
		}
		return render(request, 'staff/uni_rating_form.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')




# ---------------------------------------
# --add university apply schedule view --
# ---------------------------------------
def apply_schedule(request, schedule_id):
	if request.user.is_staff or request.user.is_superuser:
		university = University.objects.get(id=schedule_id)
		instance = get_object_or_404(ApplySchedule, uni_name=university)

		# form to add apply schedule details
		form = ApplyScheduleForm(request.POST or None, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('staff:universities')

		context = {
			'form': form,
			'object': instance,
		}

		return render(request, 'staff/apply_schedule_form.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ---------------------------------------
# --delete university view --
# ---------------------------------------
def ApiDeleteUniversity(request):
	if request.user.is_staff or request.user.is_superuser:    
		if request.user.is_authenticated:
			if request.GET.get('u_id'):
				uni_id = request.GET.get('u_id')
				uni_obj = University.objects.get(id=uni_id)

				data = dict()
				if uni_obj in University.objects.all():
					uni_obj.delete()
					data['remove'] = 'success'
					university_list = University.objects.all()

					# paginator
					page = request.GET.get('page', 1)
					paginator = Paginator(university_list, 5)
					try:
						universities = paginator.page(page)
					except PageNotAnInteger:
						universities = paginator.page(1)
					except EmptyPage:
						universities = paginator.page(paginator.num_pages)

					data['html_uni_list'] = render_to_string(
						'staff/uni_list.html', {'object': universities}
					)

				return JsonResponse(data)


		return JsonResponse({
			'remove': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')



# ----------------------------------------
# ------------Departments View----------
# ----------------------------------------
def departments(request):
	if request.user.is_staff or request.user.is_superuser:
		university_list = University.objects.all().order_by('name')
		faculties = Faculty.objects.all().order_by('f_name')
		departments = Department.objects.all().order_by('dept_name')

		query = request.GET.get("q")
		if query:
			university_list = university_list.filter(
				Q(name__icontains=query) |
				Q(category__icontains=query)
			).distinct()

		# paginator
		paginator = Paginator(university_list, 1)
		page = request.GET.get('page')
		try:
			university = paginator.page(page)
		except PageNotAnInteger:
			university = paginator.page(1)
		except EmptyPage:
			university = paginator.page(paginator.num_pages)
		# paginator end

		context = {
			'university': university,
			'faculties': faculties,
			'departments': departments,
		}

		return render(request, 'staff/departments.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ------------------------------------------
# -------------Add Department View----------
# ------------------------------------------
def addDepartment(request, id):
	if request.user.is_staff or request.user.is_superuser:
		faculty = Faculty.objects.get(id=id)
		university = faculty.uni_name
		if request.method == 'POST':
			form = DepartmentAddForm(request.POST or None)

			if form.is_valid():
				instance = form.save(commit=False)
				instance.uni_name = university
				instance.faculty = faculty
				instance.save()
				return redirect('staff:departments')

		else:
			form = DepartmentAddForm()

		context = {
			'form': form,
		}

		return render(request, 'staff/add_department.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ------------------------------------------
# ----------- Edit Departments -------------
# ------------------------------------------
def edit_department(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(Department, id=id)
		
		form = DepartmentAddForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('staff:departments')

		context = {
			'form': form,
		}
		return render(request, 'staff/add_department.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ---------------------------------------
# ------- Delete Department View --------
# ---------------------------------------
def ApiDeleteDepartment(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('dept_id'):
			department_id = request.GET.get('dept_id')
			dept_obj = Department.objects.get(id=department_id)

			data = dict()
			if dept_obj in Department.objects.all():
				dept_obj.delete()
				data['remove'] = 'success'
				university_list = University.objects.all().order_by('name')
				faculties = Faculty.objects.all().order_by('f_name')
				departments = Department.objects.all().order_by('dept_name')

				# paginator
				paginator = Paginator(university_list, 1)
				page = request.GET.get('page')
				try:
					university = paginator.page(page)
				except PageNotAnInteger:
					university = paginator.page(1)
				except EmptyPage:
					university = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'university': university,
					'faculties': faculties,
					'departments': departments,
				}

				data['html_depts_list'] = render_to_string(
					'staff/department_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'remove': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')




# ----------------------------------------
# ------------Add Faculty Views-----------
# ----------------------------------------
def addFaculty(request, uni_id):
	if request.user.is_staff or request.user.is_superuser:
		university = University.objects.get(id=uni_id)
		if request.method == 'POST':
			form = FacultyAddForm(request.POST or None)

			if form.is_valid():
				instance = form.save(commit=False)
				instance.uni_name = university
				instance.save()
				return redirect('staff:departments')

		else:
			form = FacultyAddForm()

		context = {
			'form': form,
		}

		return render(request, 'staff/add_faculty.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ---------------------------------------
# ------------ Edit Faculty -------------
# ---------------------------------------
def edit_faculty(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(Faculty, id=id)
		
		form = FacultyAddForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('staff:departments')

		context = {
			'form': form,
		}
		return render(request, 'staff/add_faculty.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')


# ---------------------------------------
# -------- Delete Faculty View ----------
# ---------------------------------------
def ApiDeleteFaculty(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('fac_id'):
			faculty_id = request.GET.get('fac_id')
			faculty_obj = Faculty.objects.get(id=faculty_id)

			data = dict()
			if faculty_obj in Faculty.objects.all():
				faculty_obj.delete()
				data['remove'] = 'success'
				university_list = University.objects.all().order_by('name')
				faculties = Faculty.objects.all().order_by('f_name')
				departments = Department.objects.all().order_by('dept_name')

				# paginator
				paginator = Paginator(university_list, 1)
				page = request.GET.get('page')
				try:
					university = paginator.page(page)
				except PageNotAnInteger:
					university = paginator.page(1)
				except EmptyPage:
					university = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'university': university,
					'faculties': faculties,
					'departments': departments,
				}

				data['faculty_list'] = render_to_string(
					'staff/department_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'remove': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')


# ----------------------------------------
# ------------Add Unit Views--------------
# ----------------------------------------
def units(request):
	if request.user.is_staff or request.user.is_superuser:	
		university_list = University.objects.all()
		units = Unit.objects.all()	

		query = request.GET.get("q")
		if query:
			university_list = university_list.filter(
				Q(name__icontains=query) |
				Q(category__icontains=query)
			).distinct()

		# paginator
		paginator = Paginator(university_list, 5)
		page = request.GET.get('page')
		try:
			universities = paginator.page(page)
		except PageNotAnInteger:
			universities = paginator.page(1)
		except EmptyPage:
			universities = paginator.page(paginator.num_pages)
		# paginator end

		context = {
			'universities': universities,
			'units': units
		}
		return render(request, 'staff/units.html', context)
	else:
		return render(request, 'staff/page_not_found.html')


# ----------------------------------------
# ------------Add Unit Views--------------
# ----------------------------------------
def addUnit(request, id):
	if request.user.is_staff or request.user.is_superuser:
		university = University.objects.get(id=id)
		if request.method == 'POST':
			form = UnitAddForm(request.POST or None, request.FILES or None)

			if form.is_valid():
				instance = form.save(commit=False)
				instance.uni_name = university
				instance.save()
				return redirect('staff:units')
			else:
				print('not valid')
		else:
			form = UnitAddForm()


		context = {
			'form': form,
		}

		return render(request, 'staff/add_unit.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ---------------------------------------
# --------------Edit Unit----------------
# ---------------------------------------
def editUnit(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(Unit, id=id)
		
		form = UnitAddForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('staff:units')

		context = {
			'form': form,
		}
		return render(request, 'staff/add_unit.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# ---------------------------------------
# ----------- delete unit view ----------
# ---------------------------------------
def ApiDeleteUnit(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('unit_id'):
			unit_id = request.GET.get('unit_id')
			unit_obj = Unit.objects.get(id=unit_id)

			data = dict()
			if unit_obj in Unit.objects.all():
				unit_obj.delete()
				data['remove'] = 'success'
				university_list = University.objects.all()
				units = Unit.objects.all()			
				
				# paginator
				paginator = Paginator(university_list, 5)
				page = request.GET.get('page')
				try:
					universities = paginator.page(page)
				except PageNotAnInteger:
					universities = paginator.page(1)
				except EmptyPage:
					universities = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'universities': universities,
					'units': units,
				}
				data['html_unit_list'] = render_to_string(
					'staff/unit_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'remove': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')



# --------------------------------------
# ----------- Feedbacks Viw ------------
# --------------------------------------
def feedbacks(request):
	if request.user.is_staff or request.user.is_superuser:
		feedback_list = Feedback.objects.filter(approval=False).order_by('-send_date')

		# paginator
		paginator = Paginator(feedback_list, 3)
		page = request.GET.get('page')
		try:
			feedbacks = paginator.page(page)
		except PageNotAnInteger:
			feedbacks = paginator.page(1)
		except EmptyPage:
			feedbacks = paginator.page(paginator.num_pages)
		# paginator end

		context = {
			'feedbacks': feedbacks,
		}

		return render(request, 'staff/feedbacks.html', context)
	else:
		return render(request, 'staff/page_not_found.html')


# -----------------------------------------
# --------- Approval Feedback view --------
# -----------------------------------------
def ApiApproveFeedback(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('feedback_id'):
			feedback_id = request.GET.get('feedback_id')
			feedback_obj = Feedback.objects.get(id=feedback_id)

			data = dict()
			if feedback_obj in Feedback.objects.all():
				feedback_obj.approval = True
				feedback_obj.save()
				data['approve'] = 'success'
				feedback_list = Feedback.objects.filter(approval=False).order_by('-send_date')		
				# paginator
				paginator = Paginator(feedback_list, 3)
				page = request.GET.get('page')
				try:
					feedbacks = paginator.page(page)
				except PageNotAnInteger:
					feedbacks = paginator.page(1)
				except EmptyPage:
					feedbacks = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'feedbacks': feedbacks,
				}
				data['html_feedback_list'] = render_to_string(
					'staff/feedback_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'approve': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')


# ---------------------------------------
# --------- delete feedback view --------
# ---------------------------------------
def ApiDeleteFeedback(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('feedback_id'):
			feedback_id = request.GET.get('feedback_id')
			feedback_obj = Feedback.objects.get(id=feedback_id)

			data = dict()
			if feedback_obj in Feedback.objects.all():
				feedback_obj.delete()

				data['remove'] = 'success'
				feedback_list = Feedback.objects.filter(approval=False).order_by('-send_date')		
				# paginator
				paginator = Paginator(feedback_list, 3)
				page = request.GET.get('page')
				try:
					feedbacks = paginator.page(page)
				except PageNotAnInteger:
					feedbacks = paginator.page(1)
				except EmptyPage:
					feedbacks = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'feedbacks': feedbacks,
				}
				data['html_feedback_list'] = render_to_string(
					'staff/feedback_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'remove': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')



# --------------------------------------
# ----------- Message Viw --------------
# --------------------------------------
def queries(request):
	if request.user.is_staff or request.user.is_superuser:
		message_list = Contact.objects.filter(replied=False).order_by('-msg_send_date')				

		# paginator
		paginator = Paginator(message_list, 3)
		page = request.GET.get('page')
		try:
			messages = paginator.page(page)
		except PageNotAnInteger:
			messages = paginator.page(1)
		except EmptyPage:
			messages = paginator.page(paginator.num_pages)
		# paginator end

		context = {
			'messages': messages,
		}

		return render(request, 'staff/messages.html', context)
	else:
		return render(request, 'staff/page_not_found.html')



# --------------------------------------------
# -------------- Reply Message ---------------
# --------------------------------------------
def replyMessage(request, id):
	if request.user.is_staff or request.user.is_superuser:
		instance = get_object_or_404(Contact, id=id)

		if request.method == 'POST':
			form = ReplyMessage(request.POST or None, instance=instance)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.replied = True
				instance.save()
				return redirect('staff:queries')

		else:
			form = ReplyMessage()

		context = {
			'form': form,
			'instance': instance
		}

		return render(request, 'contact/reply.html', context)
	
	else:
		return render(request, 'staff/page_not_found.html')



# -----------------------------------------
# --------- Replied Message view ----------
# -----------------------------------------
def ApiRepliedMessage(request):    
	if request.user.is_staff or request.user.is_superuser:
		if request.GET.get('message_id'):
			message_id = request.GET.get('message_id')
			message_obj = Contact.objects.get(id=message_id)

			data = dict()
			if message_obj in Contact.objects.all():
				message_obj.replied = True
				message_obj.save()
				data['replied'] = 'success'
				message_list = Contact.objects.filter(replied=False).order_by('-msg_send_date')						

				# paginator
				paginator = Paginator(message_list, 3)
				page = request.GET.get('page')
				try:
					messages = paginator.page(page)
				except PageNotAnInteger:
					messages = paginator.page(1)
				except EmptyPage:
					messages = paginator.page(paginator.num_pages)
				# paginator end

				context = {
					'messages': messages,
				}
				data['html_message_list'] = render_to_string(
					'staff/message_list.html', context
				)

			return JsonResponse(data)


		return JsonResponse({
			'replied': 'error'
		})
	
	else:
		return render(request, 'staff/page_not_found.html')




# ------------------------------------------------
# send mail if interested unit deadling is coming 
# ------------------------------------------------

def sendMail(request):
	if request.user.is_staff or request.user.is_superuser:
		queryset = InterestedUni.objects.all()
		today = datetime.now().date()
		subject = 'University Admission Assistant'
		from_email = EMAIL_HOST_USER

		for interested in queryset:
			for unit in interested.units.all():
				if ((unit.apply_dead.date() - today) <= timedelta(7)) and ((unit.apply_dead.date() - today) >= timedelta(0)):
					message='Applicatioin for '+str(unit.uni_name)+' Unit '+str(unit.unit_name)+' is going to be closed soon. Application deadline is '+str(unit.apply_dead.date())+' .If you are stil interested to apply please visit our website http://127.0.0.1:8000/ Thank You.'
					to_email = [interested.user.email]

					send_mail(
						subject = subject,
						from_email = from_email,
						recipient_list = to_email,
						message = message,
					    fail_silently=False,
					)

					return render(request, 'staff/send_mail.html')
	else:
		return render(request, 'staff/page_not_found.html')