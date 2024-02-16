from django.urls import path
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("About",views.About,name="About")
]
