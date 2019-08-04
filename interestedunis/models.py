from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from universities.models import Unit

User = settings.AUTH_USER_MODEL

class InterestedUni(models.Model):
	user	  = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	units  	  = models.ManyToManyField(Unit, blank=True)
	total     = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated   = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

def create_interested(sender, **kwargs):
    if kwargs['created']:
        interested = InterestedUni.objects.create(user=kwargs['instance'])

post_save.connect(create_interested, sender=User)


def pre_save_interested_reciver(sender, instance, action, *args, **kwargs):
	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		units = instance.units.all()
		total = 0
		for u in units:
			total += u.apply_fees
		instance.total = total
		instance.save()

m2m_changed.connect(pre_save_interested_reciver, sender=InterestedUni.units.through)