from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.http import HttpResponse

def Admin_Ony(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == None:
            return view_func(request,*args,**kwargs)
        if group == "patient":
            return view_func(request,*args,**kwargs)
        if group == "staff":
            return redirect("StaffIndex")
        if group == "doctor":
            return redirect("DoctorIndex")
        if group == "admin":
            return redirect("AdminIndex")
    return wrapper_func