from appliedunis.choices import *
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from universities.models import Unit
from uaa.utils import unique_application_id_generator



# -----------------------------------------------
# ----------- Apply Application Model -----------
# -----------------------------------------------
class ApplyApplication(models.Model):
    user	  = models.ForeignKey(User, on_delete=models.CASCADE)
    unit      = models.ForeignKey(Unit, on_delete=models.CASCADE)
    application_id = models.CharField(max_length=120, blank=True)
    status         = models.CharField(max_length=120, default='Requested', choices=APPLY_STATUS_CHOICES)
    admit_card     = models.FileField(upload_to='AdmitCards/%Y/%m/%d/', blank=True)
    creation_date  = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
    taken_by       = models.CharField(max_length=120, blank=True, null=True)
    # txnID, Billnumber/applicationID, userID & password (charfield)
    # file_with_id (filefield)
    # applicable/notapplicable status(not required now)
    # result: merit position(not required now)
    # seatplan, eligible candidate list, choice form link download link direct from university website page
    information    = models.TextField(max_length=500, blank=True, null=True)

    
    def __str__(self):
        return self.application_id

def pre_save_create_application_id(sender, instance, *args, **kwargs):
    if not instance.application_id:
        instance.application_id = unique_application_id_generator(instance)

pre_save.connect(pre_save_create_application_id, sender=ApplyApplication)





# basic admission requirements : 
#     check ssc hsc passing year(gte required year)
#     check students group with required group
#     group wise individual gpa checking
#     specified subject total checking and individual checking(math/higher math, physics, chemistry, biology, english, bangla)

    
#     different notice can be uploaded by following: create a model named notice. make a charfield which will contain all link of a university notices.


# ---------------------------------------
# -------- Notification Model -----------
# ---------------------------------------
class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created  = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)


    def __str__(self):
        return str(self.message)

    # def get_absolute_url(self):
    #     return reverse('accounts:single_application', kwargs={"username": self.receiver, "id": self.application_id})   