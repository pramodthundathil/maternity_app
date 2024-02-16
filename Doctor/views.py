from django.shortcuts import render,redirect
from django.contrib import messages
from Home.forms import UserAddForm
from .forms import DoctorListAddForm, WorkoutaddForm,FoodaddForm
from django.contrib.auth.models import User,Group
from Bookings.models import Booking
from Patient.models import PatientProfile, TreatmetHistory
from .models import Workout, FoodRecom

# Create your views here.

def DoctorIndex(request):
    bookings = Booking.objects.all()
    context = {
        "bookings":bookings
    }
    return render(request,"doctor/doctorindex.html",context)

def AddDoctor(request):
    form = UserAddForm()
    dfrom = DoctorListAddForm
    
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')

            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('AddDoctor')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('AddDoctor')
            
            else:
                new_user = form.save()
                group = Group.objects.get(name='doctor')
                new_user.groups.add(group) 
                new_user.save()
                dform = DoctorListAddForm(request.POST)
                if dform.is_valid():
                    doctor = dform.save()
                    doctor.Doctirid = new_user
                    doctor.save()
                
                messages.success(request,"Doctor Created Successfully...")
                return redirect('AddDoctor')
    context = {
        'form':form,
        "dform":DoctorListAddForm
    }
    return render(request,"doctor/adddoctor.html",context)

def AddSummery(request,pk):
    book = Booking.objects.get(id = pk)
    Patient = PatientProfile.objects.get(PatientId =  book.user)
    if request.method == "POST":
        Disease = request.POST["dises"]
        Treatment = request.POST["treat"]
        Medicines = request.POST["Medicines"]
        
        treat = TreatmetHistory.objects.create(Disease = Disease,Treatmet = Treatment,Medicine = Medicines,Doctor = request.user,Patient = Patient )
        treat.save()
        messages.info(request,"Summery Updated")
        
    return redirect("BookingView",pk = pk)


def Doctorutility(request):
    form = FoodaddForm()
    form1 = WorkoutaddForm()
    work = Workout.objects.all() 
    food = FoodRecom.objects.all()
    if request.method == "POST":
        form = FoodaddForm(request.POST,request.FILES)
        if form.is_valid():
            med  = form.save()
            med.save()
            messages.info(request,"Data saved")
            return redirect("Doctorutility")
        else:
           messages.info(request,"Data not saved")
           return redirect("Doctorutility")

    context = {
        "form":form,
        "form1":form1,
        "work":work,
        "food":food
    } 
    return render(request,"doctor/foodandorkoutadd.html",context)


def Workoutsave(request):
    
    if request.method == "POST":
        form = WorkoutaddForm(request.POST,request.FILES)
        if form.is_valid():
            med  = form.save()
            med.save()
            messages.info(request,"Data saved")
            return redirect("Doctorutility")
        else:
           messages.info(request,"Data not saved")
           return redirect("Doctorutility")
    return redirect("Doctorutility")

def Deleteworkout(request,pk):
    work = Workout.objects.get(id = pk)
    work.workoutimage.delete()
    work.delete()
    return redirect("Doctorutility")

def DeleteFood(request,pk):
    work = FoodRecom.objects.get(id = pk)
    work.foodimage.delete()
    work.delete()
    return redirect("Doctorutility")
    