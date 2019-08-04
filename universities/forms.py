from django import forms
from universities.models import *
from .choices import *
from ckeditor.widgets import CKEditorWidget

# ----------------------------
# Form for University basi info add
# ----------------------------
class UniBasicAddForm(forms.ModelForm):
	name 		= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	category	= forms.ChoiceField(
					choices = UNIVERSITY_CATEGORY_CHOICE, 
					initial='University Type', widget=forms.Select(attrs={'class': 'form-control',}), required=True)

	about		= forms.CharField(required=False, widget=CKEditorWidget(attrs={'class': 'form-control',}))

	rank 		= forms.IntegerField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	established = forms.IntegerField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	address 	= forms.CharField(required=False, max_length= 500, widget=forms.Textarea(attrs={'class': 'form-control md-textarea',}))

	website 	= forms.CharField(max_length=200, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	email 		= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	phone 		= forms.CharField(max_length=20, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))

	# postal_code = forms.CharField(max_length=10, required=False, widget=forms.TextInput(
	# 				attrs={'class': 'form-control',}))
	logo		= forms.FileField(required=False)

	class Meta:
		model = University
		fields = [
			'name',
			'category', 
			'about',
			'logo',
			'rank', 
			'established', 
			'address', 
			'website',
			'email',
			'phone',
		]


# ----------------------------
# Form for University rating add
# ----------------------------
class UniRatingForm(forms.ModelForm):
	quality_edu = forms.FloatField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	tuition_fee = forms.FloatField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	living 		= forms.FloatField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	transport 	= forms.FloatField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	research_innovation = forms.FloatField(required=False, widget=forms.TextInput(
							attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	extra_curricular 	= forms.FloatField(required=False, widget=forms.TextInput(
							attrs={'class': 'form-control', 'placeholder': 'Ex. 90.00'}))

	class Meta:
		model = Rating
		fields = [
			'quality_edu',
			'research_innovation',
			'tuition_fee',
			'extra_curricular',
			'living',
			'transport',
		]



# ----------------------------
# Form for Apply Schedule add
# ----------------------------
class ApplyScheduleForm(forms.ModelForm):
	apply_start = forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))

	apply_end	= forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))

	valid_list 	= forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))

	result_pub 	= forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))

	notice 		= forms.FileField(required=False)

	admit_dwon_start = forms.DateTimeField(required=True, widget=forms.DateTimeInput(
						attrs={'class': 'form-control',}))

	admit_dwon_end 	 = forms.DateTimeField(required=True, widget=forms.DateTimeInput(
						attrs={'class': 'form-control',}))
	
	class Meta:
		model = ApplySchedule
		fields = [
			'apply_start', 'apply_end', 'valid_list', 'admit_dwon_start', 'admit_dwon_end',
			'result_pub', 'notice',
		]



# ------------------------------------
# ---------Department Add Form--------
# ------------------------------------
class DepartmentAddForm(forms.ModelForm):
	dept_name  = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class':'form-control',}))
	short_form = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))
	content    = forms.CharField(required=False, widget=CKEditorWidget(attrs={'class': 'form-control',}))


	degree   = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class':'form-control',}))
	credit   = forms.IntegerField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))
	duration = forms.IntegerField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))
	language = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
					attrs={'class':'form-control',}))
	seat     = forms.IntegerField(required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))


	quality    = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))
	lab        = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))
	curriculam = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))
	extra      = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))
	success    = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))
	employ_ability = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5.00'}))


	class Meta:
		model = Department

		fields = [
			'dept_name', 'short_form', 'content',
			'degree', 'seat', 'language', 'duration', 'credit',
			'quality', 'lab', 'curriculam', 'extra', 'success', 'employ_ability',
		]


		

# --------------------------------------------
# -----------Add Faculty for University-------
# --------------------------------------------
class FacultyAddForm(forms.ModelForm):
	f_name 	 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
					attrs={'class':'form-control',}))


	class Meta:
		model = Faculty

		fields = [
			'f_name',
		]



# --------------------------------------------
# -----------Add Unit for University-------
# --------------------------------------------
class UnitAddForm(forms.ModelForm):
	unit_name = forms.CharField(max_length=12, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))	
	apply_fees = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
	seat = forms.CharField(max_length=12, required=False, widget=forms.TextInput(
				attrs={'class': 'form-control'}))
	apply_dead = forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))
	exam_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(
					attrs={'class': 'form-control',}))

	science    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	commerce   = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	humanities = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))

	ssc_year = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
	hsc_year = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
	science_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	science_tgpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	commerce_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',})) 
	commerce_tgpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	arts_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	arts_tgpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))

	phy_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	chem_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	math_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	bio_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	en_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	ban_gpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))
	tgpa = forms.FloatField(required=False, initial=0.00, widget=forms.TextInput(attrs={'class': 'form-control',}))

	notice 		= forms.FileField(required=False)
	seat_plan	= forms.FileField(required=False)
	result 		= forms.FileField(required=False)

	class Meta:
		model = Unit

		fields = [
			'unit_name', 
			'apply_fees', 
			'seat', 
			'apply_dead', 
			'exam_date',

			'science', 
			'commerce', 
			'humanities', 
			'ssc_year', 
			'hsc_year', 
			'science_gpa',
			'science_tgpa', 
			'commerce_gpa', 
			'commerce_tgpa', 
			'arts_gpa',
			'arts_tgpa',

			'phy_gpa', 
			'chem_gpa', 
			'math_gpa', 
			'bio_gpa', 
			'en_gpa',
			'ban_gpa',
			'tgpa',

			'notice', 
			'seat_plan', 
			'result'
		]