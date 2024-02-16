from django.db import models
from Doctor.models import DoctorList
from django.contrib.auth.models import User
from Patient.models import PatientProfile


# Create your models here.
class Booking(models.Model):
    Patinet = models.ForeignKey(PatientProfile,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Date = models.DateField(auto_now_add=False)
    Time = models.TimeField(auto_now_add=False)
    Doctor = models.ForeignKey(DoctorList,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return "{} {}".format(self.Date,self.Time)