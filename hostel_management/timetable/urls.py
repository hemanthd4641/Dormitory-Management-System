from django.urls import path
from . import views
app_name = 'timetable'
urlpatterns = [
    path('',views.viewTimetable,name='Foodtimetable'),
    path('update/<int:pk>',views.update_timetable_view,name='update')
]