from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.urls import reverse
from django.utils.text import slugify
from uaa.utils import short_name_generator
from ckeditor.fields import RichTextField
from universities.choices import *


# ---------------------------------
#--------university model----------
#----------------------------------
class University(models.Model):
	name 	    = models.CharField(max_length=255, blank=True, null=True)
	category    = models.CharField(max_length=120, choices=UNIVERSITY_CATEGORY_CHOICE, blank=True, null=True)
	about 		= RichTextField(blank=True, null=True)
	slug 		= models.SlugField(unique=True)
	rank 		= models.IntegerField(blank=True, null=True)
	established = models.CharField(max_length=4, blank=True, null=True)
	address     = models.TextField(max_length=500, blank=True, null=True)
	website 	= models.CharField(max_length=200, blank=True, null=True)
	email		= models.CharField(max_length=255, blank=True, null=True)
	phone 		= models.CharField(max_length=20, blank=True, null=True)
	logo		= models.FileField(upload_to='Logo/', blank=True)

	class Meta:
		verbose_name = 'University'
		verbose_name_plural = 'Universities'
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('universities:university', kwargs={"slug": self.slug})    

	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while University.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()




# ---------------------------------
# ---------Faculty model-----------
# ---------------------------------
class Faculty(models.Model):
	uni_name = models.ForeignKey(University, blank=True, null=True, on_delete=models.CASCADE)
	f_name = models.CharField(max_length=255, blank=True, null=True)	
	# depts = models.ManyToManyField(Department, blank=True)

	class Meta:
		verbose_name = 'Faculty'
		verbose_name_plural = 'Faculties'

	def __str__(self):
		return self.f_name
# end of faculty model




# --------------------------------------
#----------- department model-----------
# --------------------------------------
class Department(models.Model):
	uni_name   = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
	faculty    = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
	dept_name  = models.CharField(max_length=255, blank=True, null=True)
	short_form = models.CharField(max_length=255, blank=True, null=True)
	slug       = models.SlugField(unique=True, blank=True)

	content	   = RichTextField(blank=True, null=True)
	degree     = models.CharField(max_length=255, blank=True, null=True)
	credit	   = models.IntegerField(blank=True, null=True)
	duration   = models.IntegerField(blank=True, null=True)
	language   = models.CharField(max_length=50, blank=True, null=True)
	seat       = models.IntegerField(blank=True, null=True)
	

	# ------------Department Ratings---------------------
	quality    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	lab		   = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	curriculam = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	# Extra curriculam
	extra 	   = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	# Success of Graduates
	success    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	# Employ Ability of Graduates
	employ_ability = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	#---------------Department Ratings End------------------
	

	# semester_fee
	# course_fee

	def __str__(self):
		return str(self.short_form)

	def average(self):
		total = self.quality + self.lab + self.curriculam + self.extra + self.success + self.employ_ability
		average = round(total/6, 2)
		return average

	def save(self, *args, **kwargs):
		self.slug = '-'.join((slugify(self.uni_name.name), slugify(self.short_form)))
		super(Department, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('universities:department', args=[self.slug])
# end of department models


# ----------------------------------
# ----------- Unit Model -----------
# ----------------------------------
class Unit(models.Model):
	uni_name   = models.ForeignKey(University, blank=True, null=True, on_delete=models.CASCADE)
	unit_name  = models.CharField(max_length=12, blank=True, null=True)
	seat	   = models.CharField(max_length=12, blank=True, null=True)
	apply_dead = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	exam_date  = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	apply_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	science    = models.BooleanField(default=False)
	commerce   = models.BooleanField(default=False)
	humanities = models.BooleanField(default=False)

	ssc_year   = models.CharField(max_length=20, blank=True, null=True)
	hsc_year   = models.CharField(max_length=20, blank=True, null=True)
	
	science_gpa   = models.FloatField(default=0.00, blank=True, null=True)
	science_tgpa  = models.FloatField(default=0.00, blank=True, null=True)

	commerce_gpa  = models.FloatField(default=0.00, blank=True, null=True)
	commerce_tgpa = models.FloatField(default=0.00, blank=True, null=True)

	arts_gpa 	  = models.FloatField(default=0.00, blank=True, null=True)
	arts_tgpa	  = models.FloatField(default=0.00, blank=True, null=True)

	phy_gpa	   = models.FloatField(default=0.00, blank=True, null=True)
	chem_gpa   = models.FloatField(default=0.00, blank=True, null=True)
	math_gpa   = models.FloatField(default=0.00, blank=True, null=True)
	bio_gpa    = models.FloatField(default=0.00, blank=True, null=True)
	en_gpa     = models.FloatField(default=0.00, blank=True, null=True)
	ban_gpa    = models.FloatField(default=0.00, blank=True, null=True)
	tgpa       = models.FloatField(default=0.00, blank=True, null=True)

	notice 	   = models.FileField(upload_to='Admissoin Notice/%Y/%m/%d', blank=True)
	seat_plan  = models.FileField(upload_to='Admissoin Notice/%Y/%m/%d', blank=True)
	result     = models.FileField(upload_to='Admissoin Notice/%Y/%m/%d', blank=True)

	def __str__(self):
		return self.unit_name
# end of unit model



# ----------------------------------------
# cost of living for a particular university
# ----------------------------------------
"""class CostOfLiving(models.Model):
	uni_name = models.ForeignKey(University, on_delete=models.CASCADE)
	rent_utilities = models.CharField(max_length=100, blank=True, null=True)
	food_drinks = models.CharField(max_length=100, blank=True, null=True)
	learing = models.CharField(max_length=100, blank=True, null=True)
	transport = models.CharField(max_length=100, blank=True, null=True)
	internet = models.CharField(max_length=100, blank=True, null=True)
	others = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.uni_name"""



# ------------------------------------------
# rating of a university based on some criteria
# -------------------------------------------
class Rating(models.Model):
	uni_name 	= models.ForeignKey(University, on_delete=models.CASCADE)
	quality_edu = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	research_innovation = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	tuition_fee = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	extra_curricular 	= models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	# environment = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	living      = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	transport 	= models.DecimalField(default=0.00, max_digits=5, decimal_places=2)

	def __str__(self):
		return self.uni_name.name

	def average(self):
		total = self.quality_edu + self.research_innovation + self.tuition_fee + self.extra_curricular + self.living + self.transport
		average = round(total/6, 2)
		return average


# --------------------------------------------
# ------------admission time table------------
# --------------------------------------------
class ApplySchedule(models.Model):
	uni_name = models.ForeignKey(University, on_delete=models.CASCADE)
	apply_start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	apply_end 	= models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	valid_list 	= models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	result_pub 	= models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	# unit = models.ManyToManyField(Unit, blank=False)
	# exam_time	= RichTextField(blank=True, null=True) or image/file field
	notice		= models.FileField(upload_to='Admissoin Notice/%Y/%m/%d', blank=True)
	admit_dwon_start  = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	admit_dwon_end    = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	# use RichTextField for showing all important dates in a tabular format 
	

	def __str__(self):
		return self.uni_name.name

	# def delete(self, *args, **kwargs):
	# 	self.notice.delete()
	# 	super().delete(*args, **kwargs) 