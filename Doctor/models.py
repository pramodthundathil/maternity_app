from django.db import models
from django.contrib.auth.models import User


class DoctorList(models.Model):
    
    Doctirid = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    DoctorName = models.CharField(max_length=255)
    Doctor_spec = models.CharField(max_length=255)
    Doctor_Edu = models.CharField(max_length=255)
    
    def __str__(self):
        return "Dr.{} {}, {}".format(self.DoctorName,self.Doctor_Edu,self.Doctor_spec)
    
class FoodRecom(models.Model):

    options = (
        ("1-4 weeks","1-4 weeks"),
        ("5-8 weeks","5-8 weeks"),
        ("9-13 weeks","9-13 weeks"),
        ("14-17 weeks","14-17 weeks"),
        ("18-22 weeks","18-22 weeks"),
        ("23-27 weeks","23-27 weeks"),
        ("28-31 weeks","28-31 weeks"),
        ("32-35 weeks","32-35 weeks"),
        ("36-40 weeks","36-40 weeks"),
 
    )
    options1 = (("Carbohydrates","Carbohydrates"), ("Proteins","Proteins"), ("Fats","Fats"), ("Vitamins","Vitamins"), ("Minerals","Minerals"), ("Dietary fiber","Dietary fiber"), ("Water","Water"))

    food = models.CharField(max_length = 255)
    foodimage = models.FileField(upload_to="food_image")
    calories = models.FloatField()
    nutrition = models.CharField(max_length = 255,choices = options1)
    timester = models.CharField(max_length = 255, choices = options)
    
class Workout(models.Model):

    options = (
        ("1-4 weeks","1-4 weeks"),
        ("5-8 weeks","5-8 weeks"),
        ("9-13 weeks","9-13 weeks"),
        ("14-17 weeks","14-17 weeks"),
        ("18-22 weeks","18-22 weeks"),
        ("23-27 weeks","23-27 weeks"),
        ("28-31 weeks","28-31 weeks"),
        ("32-35 weeks","32-35 weeks"),
        ("36-40 weeks","36-40 weeks"),
 
    )
    
    workoutname = models.CharField(max_length = 255)
    description = models.CharField(max_length = 1000)
    workoutimage = models.FileField(upload_to="workout_image")
    timester = models.CharField(max_length = 255, choices = options)
    
    
