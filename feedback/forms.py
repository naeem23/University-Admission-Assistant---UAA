from django import forms
from .models import Feedback


# -------------------------------------
# ---------- Feedback Model -----------
# -------------------------------------
class FeedbackForm(forms.ModelForm):
	name = forms.CharField(max_length=55, required=False, widget=forms.TextInput(
					attrs={'class': 'form-control',}))
	email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

	review = forms.CharField(required=False, max_length= 500, widget=forms.Textarea(attrs={'class': 'form-control md-textarea',}))
	message = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={'class': 'form-control md-textarea',}))

	# oe for overall Experience
	oe_very_good  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	oe_good 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	oe_fair 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	oe_poor 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))

	# tr for timely response
	tr_very_good  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	tr_good 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	tr_fair 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	tr_poor 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))

	# s for our support
	s_very_good = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	s_good 	    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	s_fair 	    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	s_poor 	    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))

	# os for overall satisfaction
	os_very_good  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	os_good 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	os_fair 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	os_poor 	  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input',}))
	
	class Meta:
		model = Feedback
		fields = [
			'name', 'email', 'review', 'message',
			'oe_very_good', 'oe_good', 'oe_fair', 'oe_poor',
			'tr_very_good', 'tr_good', 'tr_fair', 'tr_poor',
			's_very_good', 's_good', 's_fair', 's_poor',
			'os_very_good', 'os_good', 'os_fair', 'os_poor',
		]
			
	
		