from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from Patient.models import PatientProfile 

# Create your views here.

@login_required(login_url="SignIn")
def MakeAppointment(request):
    form = BookingForm()
    book = Booking.objects.filter(user = request.user)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("Date")
            time = form.cleaned_data.get("Time")
            
            if Booking.objects.filter(Date = date, Time= time).exists():
                messages.info(request,"Slot Not Avileable")
                return redirect("MakeAppointment")
            
            else:
                val = form.save()
                val.user = request.user
                try:
                    val.Patinet = PatientProfile.objects.get(PatientId = request.user)
                    val.save()
                except:
                    val.save()
                messages.info(request,"Booking Done")
                return redirect("MakeAppointment")
            
    return render(request,"makeappointment.html",{"form":form,"book":book})

def DeleteBooking(request,pk):
    booking = Booking.objects.get(id = pk)
    booking.delete()
    messages.info(request,"Booking Deleted")
    return redirect("StaffIndex")
