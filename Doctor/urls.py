from django.urls import path
from .import views

urlpatterns = [
    path("DoctorIndex",views.DoctorIndex,name="DoctorIndex"),
    path("AddDoctor",views.AddDoctor,name="AddDoctor"),
    path("AddSummery/<str:pk>",views.AddSummery,name="AddSummery"),
    path("Doctorutility",views.Doctorutility,name="Doctorutility"),
    path("Workoutsave",views.Workoutsave,name="Workoutsave"),
    path("Deleteworkout/<int:pk>",views.Deleteworkout,name="Deleteworkout"),
    path("DeleteFood/<int:pk>",views.DeleteFood,name="DeleteFood"),

    
]

