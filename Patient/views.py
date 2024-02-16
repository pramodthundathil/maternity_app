from django.shortcuts import render,redirect
from django.contrib import messages
from Bookings.models import Booking
from Patient.models import PatientProfile,TreatmetHistory
from StaffApp.models import Product
from datetime import datetime, timedelta, date
from Doctor.models import FoodRecom, Workout

# Create your views here.

def MyAppointments(request):
    book = Booking.objects.filter(user = request.user)
    context = {
        "book":book
    }
    return render(request,'myappointments.html',context)

def CancelBooking(request,pk):
    Booking.objects.get(id = pk).delete()
    messages.info(request,"Booking Cancelled")
    return redirect('Index')

def TreatmentHistory(request):
    patientpro = PatientProfile.objects.get(PatientId = request.user)
    treat = TreatmetHistory.objects.filter(Patient = patientpro)
    context = {
        "treat":treat
    }
    return render(request,"treatmenthistory.html",context)

def ChangeMaternityStartDate(request):
    profile = PatientProfile.objects.get(PatientId = request.user)
    if request.method == "POST":
        date = request.POST['date']
        profile.maternity_start = date
        profile.save()
        return redirect("MyMaternity")


def MyMaternity(request):
    profile = PatientProfile.objects.get(PatientId = request.user)
    maternityatart = profile.maternity_start
    today = date.today()
    monday1 = (maternityatart - timedelta(days=maternityatart.weekday()))
    monday2 = (today - timedelta(days=today.weekday()))

    print ('Weeks:', (monday2 - monday1).days / 7)
    weeks = int((monday2 - monday1).days / 7)
    val = 0
    if weeks >=0 and weeks <= 4:
        week = "1-4 weeks"
    elif weeks >4 and weeks <=8:
        week = "5-8 weeks"
    elif weeks >8 and weeks <=13:
        week = "9-13 weeks"
    elif weeks >9 and weeks <=17:
        week = "14-17 weeks"
    elif weeks >17 and weeks <=22:
        week = "18-22 weeks"
    elif weeks >22 and weeks <=27:
        week = "23-27 weeks"
    elif weeks >27 and weeks <=31:
        week = "28-31 weeks"
    elif weeks >31 and weeks <=35:
        week = "32-35 weeks"
    elif weeks >26 and weeks <=40:
        week = "36-40 weeks"

    product = Product.objects.filter(timester = week)
    food = FoodRecom.objects.filter(timester = week)
    workout = Workout.objects.filter(timester = week)
    
    

    context = {
        "profile":profile,
        "product":product,
        "weeks":weeks,
        "food":food,
        "workout":workout
    }
    return render(request,"mymaternity.html",context)