from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserAddForm
from django.contrib.auth.decorators import login_required
from .decorator import Admin_Ony
from Doctor.models import DoctorList

@Admin_Ony
def Index(request):
    context = {
        "doctor":DoctorList.objects.all()
    }
    return render(request,'index.html',context)

def AdminIndex(request):
    return render(request,"admin/adminhome.html")

def SignIn(request):
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            if request.user.is_superuser == True:
                return redirect('AdminIndex')
            else:
                return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
        
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')

            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('SignUp')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('SignUp')
            
            else:
                new_user = form.save()
                new_user.save()
                
                messages.success(request,"User Created Successfully...")
                return redirect('SignIn')
    
    return render(request,"register.html",{"form":form})


def SignOut(request):
    logout(request)
    return redirect('Index')

def About(request):
    return render(request,"about.html")


