from django.forms import ModelForm
from .models import DoctorList, FoodRecom, Workout


class DoctorListAddForm(ModelForm):
    class Meta:
        model = DoctorList
        fields = ["DoctorName","Doctor_spec","Doctor_Edu"]

class FoodaddForm(ModelForm):
    class Meta:
        model = FoodRecom
        fields = "__all__"

class WorkoutaddForm(ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"