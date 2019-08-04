from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from accounts.choices import *


# -------------------------------------
# --------- UserProfile Model ---------
# -------------------------------------
class UserProfile(models.Model):
	user 		  = models.OneToOneField(User, on_delete=models.CASCADE)

	name 		  = models.CharField(max_length=255, blank=True, null=True)
	father_name   = models.CharField(max_length=255, blank=True, null=True)
	mother_name   = models.CharField(max_length=255, blank=True, null=True)
	mobile_number = models.CharField(max_length=255, blank=True, null=True)
	rocket_number = models.CharField(max_length=255, blank=True, null=True)
	image 		  = models.ImageField(upload_to='user/image', blank=True, null=True)
	signature 	  = models.ImageField(upload_to='user/signature', blank=True, null=True)
	quota		  = models.CharField(max_length=255, blank=True, null=True, choices=QUOTA_CHOICE)
	medium 		  = models.CharField(max_length=255, blank=True, null=True, choices=MEDIUM_CHOICE)
	# address

	ssc_roll 	  = models.CharField(max_length=255, blank=True, null=True)
	ssc_reg 	  = models.CharField(max_length=255, blank=True, null=True)
	ssc_pass_y 	  = models.CharField(max_length=255, blank=True, null=True)
	ssc_board 	  = models.CharField(max_length=255, blank=True, null=True, choices=BOARD_CHOICE)
	ssc_group     = models.CharField(max_length=20,  blank=True, null=True, choices=GROUP_CHOICE)
	ssc_gpa 	  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	hsc_roll 	  = models.CharField(max_length=255, blank=True, null=True)
	hsc_reg 	  = models.CharField(max_length=255, blank=True, null=True)
	hsc_pass_y 	  = models.CharField(max_length=255, blank=True, null=True)
	hsc_board 	  = models.CharField(max_length=255, blank=True, null=True, choices=BOARD_CHOICE)
	hsc_group     = models.CharField(max_length=20,  blank=True, null=True, choices=GROUP_CHOICE)
	hsc_gpa 	  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	physics       = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)
	chemistry	  = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)
	math 		  = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)
	biology		  = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)
	english		  = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)
	bangla		  = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True, null=True)


	class Meta:
		ordering = ('user',)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

