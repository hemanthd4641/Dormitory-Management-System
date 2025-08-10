from django import forms
from .models import FoodTimetable

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = FoodTimetable
        exclude = ['id'] 
