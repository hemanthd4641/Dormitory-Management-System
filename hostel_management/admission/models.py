from django.db import models
from django.contrib.auth.models import User
from hostel.models import Room

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,blank = True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null = True,blank = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, null = False , blank = True)
    password1 = models.CharField(max_length = 100, null = False , blank = True)
    password2 = models.CharField(max_length = 100, null = False, blank = True)
    dob = models.DateField()
    gender = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone_number = models.IntegerField()
    address = models.TextField()
    admission_date = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.first_name

    

class Announcements(models.Model):
    about = models.CharField(max_length=120)
    body = models.TextField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)       

    class Meta:
        ordering = ['-updated', '-created']  

    def __str__(self):
        return self.about