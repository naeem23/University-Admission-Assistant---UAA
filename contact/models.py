from django.db import models
from django.contrib.auth.models import User

# ---------------------------------
# --------- Contact Model ---------
# ---------------------------------
class Contact(models.Model):
	name    = models.CharField(max_length=55, blank=True, null=True)
	user    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	email   = models.CharField(max_length=255, blank=True, null=True)
	subject = models.CharField(max_length=255, blank=True, null=True)
	message = models.TextField(max_length=500, blank=True, null=True)
	reply   = models.TextField(max_length=500, blank=True, null=True)
	msg_send_date = models.DateTimeField(auto_now=True)
	replied = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)
		