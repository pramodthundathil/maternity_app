from django.db import models
from django.contrib.auth.models import User
from Doctor.models import DoctorList


class PatientProfile(models.Model):
    PatientId = models.ForeignKey(User,on_delete=models.CASCADE)
    PatientName = models.CharField(max_length=255,null=True)
    Place = models.CharField(max_length=255,null=True)
    PhoneNumber = models.CharField(max_length=15)
    Doctor = models.ForeignKey(DoctorList,on_delete=models.SET_NULL,null=True,blank=True)
    Treatment = models.CharField(max_length=255,null=True,blank=True)
    maternity_start = models.DateField(auto_now_add = False,null = True, blank = True)
    
    
class TreatmetHistory(models.Model):
    Patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    dateVisited = models.DateField(auto_now_add=True)
    Disease = models.CharField(max_length=1000)
    Treatmet = models.CharField(max_length=1000)
    Medicine = models.CharField(max_length=1000)
    Doctor = models.ForeignKey(User,on_delete=models.CASCADE)
    