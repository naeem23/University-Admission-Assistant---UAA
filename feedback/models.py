from django.db import models
from django.contrib.auth.models import User


# ------------------------------------
# ---------- Feedback Model ----------
# ------------------------------------
class Feedback(models.Model):
	user	= models.ForeignKey(User, on_delete=models.CASCADE)
	name 	= models.CharField(max_length=55)
	email 	= models.CharField(max_length=255)
	review	= models.TextField(max_length=500, blank=True, null=True)
	message = models.TextField(max_length=500, blank=True, null=True)

	# oe for overall Experience
	oe_very_good  = models.BooleanField(default=False)
	oe_good 	  = models.BooleanField(default=False)
	oe_fair 	  = models.BooleanField(default=False)
	oe_poor 	  = models.BooleanField(default=False)

	# tr for timely response
	tr_very_good  = models.BooleanField(default=False)
	tr_good 	  = models.BooleanField(default=False)
	tr_fair 	  = models.BooleanField(default=False)
	tr_poor 	  = models.BooleanField(default=False)

	# s for our support
	s_very_good = models.BooleanField(default=False)
	s_good 	    = models.BooleanField(default=False)
	s_fair 	    = models.BooleanField(default=False)
	s_poor 	    = models.BooleanField(default=False)

	# os for overall satisfaction
	os_very_good  = models.BooleanField(default=False)
	os_good 	  = models.BooleanField(default=False)
	os_fair 	  = models.BooleanField(default=False)
	os_poor 	  = models.BooleanField(default=False)

	approval = models.BooleanField(default=False)

	send_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user)
		
		

