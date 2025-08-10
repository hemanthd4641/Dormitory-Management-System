from django import forms
from .models import Room,RoomAllocation
from .models import RoomAllocation,Room

INPUT_CLASSES = 'form-control form-control-sm'
class Allocation(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ('user',)
class addRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_number': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'capacity': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            }