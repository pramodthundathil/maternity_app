from django.urls import path
from .import views
urlpatterns = [
    path("MyAppointments",views.MyAppointments,name="MyAppointments"),
    path("CancelBooking/<str:pk>",views.CancelBooking,name="CancelBooking"),
    path("TreatmentHistory",views.TreatmentHistory,name="TreatmentHistory"),
    path("MyMaternity",views.MyMaternity,name="MyMaternity"),
    path("ChangeMaternityStartDate",views.ChangeMaternityStartDate,name="ChangeMaternityStartDate"),

    
]
