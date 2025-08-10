from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField() 
    occupied = models.BooleanField(default=False) 

    def __str__(self):
        return f"Room {self.room_number}"

class RoomAllocation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Room {self.room.room_number} - {self.user.username}"
