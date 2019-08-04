from django import forms
from .models import UserProfile
from accounts.choices import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import re



# --------------------------------------
# -------------Signup Form--------------
# --------------------------------------
class SignupForm(forms.Form):
	username  = forms.CharField(max_length=12, required=False, widget=forms.TextInput(
				attrs={'class':'form-control',}))

	email 	  = forms.EmailField(required=False, widget=forms.TextInput(
				attrs={'class':'form-control',}))

	password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
				attrs={'class':'form-control',}))

	password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
				attrs={'class':'form-control',}))


	def clean(self):
		username  = self.cleaned_data.get('username')
		email 	  = self.cleaned_data.get('email')
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if len(username) < 1:
			raise forms.ValidationError("Please enter a valid username.")
		else:
			user_exist = User.objects.filter(username__iexact=username).exists()

			if user_exist:
				raise forms.ValidationError("This username isn't available. Please try again.")
			else:
				if len(email) < 1:
					raise forms.ValidationError("Please enter a valid email address.")
				else:
					email_correction = re.match('[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})', email)
					
					if email_correction == None:
						raise forms.ValidationError('Please enter a valid email address.')
					else: 
						email_exist = User.objects.filter(email__iexact=email).exists()
						if email_exist:
							raise forms.ValidationError("This email is taken by another account.")
						else:
							if len(password1) < 8:
								raise forms.ValidationError("Password is too short!")
							else:
								if password1 != password2:
									raise forms.ValidationError("Password not match!")

	def signup(self,request):
		username  = self.cleaned_data.get('username')
		email 	  = self.cleaned_data.get('email')
		password1 = self.cleaned_data.get('password1')

		user = User.objects.create_user(username=username, email=email)
		user.set_password(password1)

		return user



# --------------------------------------
# -------------Login Form--------------
# --------------------------------------
class LoginForm(forms.Form):
	username 	= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
		attrs={'class':'form-control',}))

	password	= forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(
		attrs={'class':'form-control',}))


	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if len(username) < 1:
			raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
		else:
			if len(password) < 8:
				raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
			else:
				user = authenticate(username=username, password=password)

				if not user or not user.is_active:
					raise forms.ValidationError("The username and password you entered didn't match. Please check and try agian.")
		return self.cleaned_data

	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		user = authenticate(username=username, password=password)

		return user




# --------------------------------------
# ----------User Profile Form-----------
# --------------------------------------
class UserProfileForm(forms.ModelForm):
	name 			= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Student's Full Name"}))

	father_name		= forms.CharField(max_length= 255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Father's Name"}))

	mother_name		= forms.CharField(max_length= 255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Mother's Name"}))

	mobile_number 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Mobile No."}))

	rocket_number	= forms.CharField(max_length= 12, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Rocekt No."}))

	image 			= forms.ImageField(required=True)

	signature 		= forms.ImageField(required=True)

	quota		 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Quota"}))

	medium		 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "English/Bangla"}))


	ssc_roll 		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Roll No."}))

	ssc_reg			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Reg No."}))

	ssc_pass_y		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Passing Year"}))

	ssc_board		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Board"}))

	ssc_group		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Group"}))

	ssc_gpa			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "GPA"}))


	hsc_roll 		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Roll No."}))

	hsc_reg			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Reg No."}))

	hsc_pass_y		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Passing Year"}))

	hsc_board		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Board"}))

	hsc_group		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Group"}))

	hsc_gpa			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "GPA"}))


	physics			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))

	chemistry		= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))

	math			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))

	biology			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))

	english			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))

	bangla			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))


	def clean(self):
		name = self.cleaned_data.get('name')
		father_name = self.cleaned_data.get('father_name')
		mother_name = self.cleaned_data.get('mother_name')
		mobile_number = self.cleaned_data.get('mobile_number')
		rocket_number = self.cleaned_data.get('rocket_number')
		image = self.cleaned_data.get('image')
		signature = self.cleaned_data.get('signature')
		quota = self.cleaned_data.get('quota')
		medium = self.cleaned_data.get('medium')

		ssc_roll = self.cleaned_data.get('ssc_roll')
		ssc_reg = self.cleaned_data.get('ssc_reg')
		ssc_pass_y = self.cleaned_data.get('ssc_pass_y')
		ssc_board = self.cleaned_data.get('ssc_board')
		ssc_group = self.cleaned_data.get('ssc_group')
		ssc_gpa = self.cleaned_data.get('ssc_gpa')

		hsc_roll = self.cleaned_data.get('hsc_roll')
		hsc_reg = self.cleaned_data.get('hsc_reg')
		hsc_pass_y = self.cleaned_data.get('hsc_pass_y')
		hsc_board = self.cleaned_data.get('hsc_board')
		hsc_group = self.cleaned_data.get('hsc_group')
		hsc_gpa = self.cleaned_data.get('hsc_gpa')


		physics = self.cleaned_data.get('physics')
		chemistry = self.cleaned_data.get('chemistry')
		math = self.cleaned_data.get('math')
		biology = self.cleaned_data.get('biology')
		english = self.cleaned_data.get('english')
		bangla = self.cleaned_data.get('bangla')

		if len(name) < 1:
			raise forms.ValidationError("Enter your full name!")
		else:
			if len(father_name) < 1:
				raise forms.ValidationError("Enter your father's name!")
			else:
				if len(mother_name) < 1:
					raise forms.ValidationError("Enter your mother's name!")
				else:
					mobile_number_exist = UserProfile.objects.filter(mobile_number__iexact=mobile_number).exists()
					if mobile_number_exist:
						raise forms.ValidationError("Mobile Number already exists")
					else:
						rocket_number_exist = UserProfile.objects.filter(rocket_number__iexact=rocket_number).exists()
						if rocket_number_exist:
							raise forms.ValidationError("Rocekt Number already exists")
						else:
							ssc_roll_exist = UserProfile.objects.filter(ssc_roll__iexact=ssc_roll).exists()
							if ssc_roll_exist:
								raise forms.ValidationError("Invalid SSC Roll No.")
							else:
								ssc_reg_exist = UserProfile.objects.filter(ssc_reg__iexact=ssc_reg).exists()
								if ssc_reg_exist:
									raise forms.ValidationError("Invalid SSC Registration No.")
								else:
									hsc_roll_exist = UserProfile.objects.filter(hsc_roll__iexact=hsc_roll).exists()
									if hsc_roll_exist:
										raise forms.ValidationError("Invalid HSC Roll No.")
									else:
										hsc_reg_exist = UserProfile.objects.filter(hsc_reg__iexact=hsc_reg).exists()
										if hsc_reg_exist:
											raise forms.ValidationError("Invalid HSC Registraion No.")
										else:
											if int(hsc_pass_y) < int(ssc_pass_y) + 2:
												raise forms.ValidationError("Please insert correct SSC/HSC passing year")

	class Meta:
		model = UserProfile
		fields = (
			'name', 'father_name', 'mother_name', 'mobile_number', 'rocket_number', 
			'image', 'signature', 'quota', 'medium', 
			'ssc_roll', 'ssc_reg', 'ssc_pass_y', 'ssc_board', 'ssc_group', 'ssc_gpa', 
			'hsc_roll', 'hsc_reg', 'hsc_pass_y', 'hsc_board', 'hsc_group', 'hsc_gpa',
			'physics', 'chemistry', 'math', 'biology', 'english','bangla')



# --------------------------------------
# ------User's BasicInformation Form-----
# --------------------------------------

class BasicInformation(forms.ModelForm):
	name 			= forms.CharField(max_length=255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control',}))
	father_name		= forms.CharField(max_length= 255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control',}))
	mother_name		= forms.CharField(max_length= 255, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control',}))
	mobile_number 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control',}))
	rocket_number	= forms.CharField(max_length= 12, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control',}))
	image 			= forms.ImageField(required=True)
	signature 		= forms.ImageField(required=True)
	quota		 	= forms.ChoiceField(choices=QUOTA_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))
	medium		 	= forms.ChoiceField(choices=MEDIUM_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))

	def clean(self):
		name = self.cleaned_data.get('name')
		father_name = self.cleaned_data.get('father_name')
		mother_name = self.cleaned_data.get('mother_name')
		mobile_number = self.cleaned_data.get('mobile_number')
		rocket_number = self.cleaned_data.get('rocket_number')
		image = self.cleaned_data.get('image')
		signature = self.cleaned_data.get('signature')
		quota = self.cleaned_data.get('quota')
		medium = self.cleaned_data.get('medium')

		if len(name) < 1:
			raise forms.ValidationError("Enter your full name!")
		else:
			if len(father_name) < 1:
				raise forms.ValidationError("Enter your father's name!")
			else:
				if len(mother_name) < 1:
					raise forms.ValidationError("Enter your mother's name!")
				else:
					mobile_number_exist = UserProfile.objects.filter(mobile_number__iexact=mobile_number).exists()
					if mobile_number_exist:
						raise forms.ValidationError("Mobile Number already exists")
					else:
						rocket_number_exist = UserProfile.objects.filter(rocket_number__iexact=rocket_number).exists()
						if rocket_number_exist:
							raise forms.ValidationError("Rocekt Number already exists")

	class Meta:
		model = UserProfile
		fields = [
			'name', 'father_name', 'mother_name', 'mobile_number',
			'rocket_number', 'image', 'signature', 'quota', 'medium'
		]
			



# --------------------------------------
# -----User's BasicInformation Form-----
# --------------------------------------
class SscInformation(forms.ModelForm):
	ssc_roll 	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 188870"}))
	ssc_reg		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 1611339025"}))
	ssc_pass_y	= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 2017"}))
	ssc_board	= forms.ChoiceField(choices=BOARD_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))
	ssc_group	= forms.ChoiceField(choices=GROUP_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))
	ssc_gpa		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 5.00"}))

	def clean(self):
		ssc_roll = self.cleaned_data.get('ssc_roll')
		ssc_reg = self.cleaned_data.get('ssc_reg')
		ssc_pass_y = self.cleaned_data.get('ssc_pass_y')
		ssc_board = self.cleaned_data.get('ssc_board')
		ssc_group = self.cleaned_data.get('ssc_group')
		ssc_gpa = self.cleaned_data.get('ssc_gpa')


		ssc_roll_exist = UserProfile.objects.filter(ssc_roll__iexact=ssc_roll).exists()
		if ssc_roll_exist:
			raise forms.ValidationError("Invalid SSC Roll No.")
		else:
			ssc_reg_exist = UserProfile.objects.filter(ssc_reg__iexact=ssc_reg).exists()
			if ssc_reg_exist:
				raise forms.ValidationError("Invalid SSC Registration No.")

	class Meta:
		model = UserProfile
		fields = [
			'ssc_roll', 'ssc_reg', 'ssc_pass_y', 
			'ssc_board', 'ssc_group', 'ssc_gpa'
		]
			



# --------------------------------------
# -----User's BasicInformation Form-----
# --------------------------------------
class HscInformation(forms.ModelForm):
	hsc_roll 		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 164792"}))
	hsc_reg			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 649187"}))
	hsc_pass_y		= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 2019"}))
	hsc_board		= forms.ChoiceField(choices=BOARD_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))
	hsc_group		= forms.ChoiceField(choices=GROUP_CHOICE, required=True, widget=forms.Select(
						attrs={'class': 'form-control',}))
	hsc_gpa			= forms.CharField(max_length= 11, required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 5.00"}))


	physics			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	chemistry		= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	math			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	biology			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	english			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	bangla			= forms.FloatField(required=False, widget=forms.TextInput(
						attrs={'class': 'form-control', 'placeholder': "Ex. 3.50"}))
	
	def clean(self):
		hsc_roll = self.cleaned_data.get('hsc_roll')
		hsc_reg = self.cleaned_data.get('hsc_reg')
		hsc_pass_y = self.cleaned_data.get('hsc_pass_y')
		hsc_board = self.cleaned_data.get('hsc_board')
		hsc_group = self.cleaned_data.get('hsc_group')
		hsc_gpa = self.cleaned_data.get('hsc_gpa')


		physics = self.cleaned_data.get('physics')
		chemistry = self.cleaned_data.get('chemistry')
		math = self.cleaned_data.get('math')
		biology = self.cleaned_data.get('biology')
		english = self.cleaned_data.get('english')
		bangla = self.cleaned_data.get('bangla')

		hsc_roll_exist = UserProfile.objects.filter(hsc_roll__iexact=hsc_roll).exists()
		if hsc_roll_exist:
			raise forms.ValidationError("Invalid HSC Roll No.")
		else:
			hsc_reg_exist = UserProfile.objects.filter(hsc_reg__iexact=hsc_reg).exists()
			if hsc_reg_exist:
				raise forms.ValidationError("Invalid HSC Registraion No.")


	class Meta:
		model = UserProfile
		fields = [
			'hsc_roll', 'hsc_reg', 'hsc_pass_y', 
			'hsc_board', 'hsc_group', 'hsc_gpa',
			'physics', 'chemistry', 'math', 'biology', 'english', 'bangla'
		]
