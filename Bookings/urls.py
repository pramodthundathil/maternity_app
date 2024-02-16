from django.urls import path 
from .import views

urlpatterns = [
    path("MakeAppointment",views.MakeAppointment,name="MakeAppointment"),
    path("DeleteBooking/<str:pk>",views.DeleteBooking,name="DeleteBooking"),
]
