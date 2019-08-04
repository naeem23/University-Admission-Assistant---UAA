from django import forms
from appliedunis.models import ApplyApplication
from appliedunis.choices import *


# ----------------------------------------
# -----Form for Apply Request Edit--------
# ----------------------------------------
class ApplyApplicationForm(forms.ModelForm):
	status		= forms.ChoiceField(
					choices=APPLY_STATUS_CHOICES, 
					widget=forms.Select(attrs={'class': 'form-control',}), 
					required=True)
	information = forms.CharField(max_length=500, required=False, widget=forms.Textarea(
					attrs={'class': 'form-control md-textarea', 
							'placeholder': 'BillID/ApplicationID, TxnID, UserID, Password'}))
	admit_card	= forms.FileField(required=False)

	class Meta:
		model = ApplyApplication
		fields = [
			'status',
			'information',
			'admit_card',
		]
			
	