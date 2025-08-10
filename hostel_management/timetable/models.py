from django.db import models

class FoodTimetable(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK, unique=True,default='Monday')
    break_fast = models.CharField(max_length=10,default='')
    lunch = models.CharField(max_length=200,default='')
    snacks = models.CharField(max_length=200,default='')
    dinner = models.CharField(max_length=200,default='')

    def __str__(self):
        return f"{self.day}"


