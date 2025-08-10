from django.urls import path
from . import views
app_name = 'hostel'
urlpatterns = [
    path('',views.index,name='index'),
    path('allocations/<int:pk>',views.allocation_view,name='allocations'),
    path('delete/<int:pk>/',views.delete,name = 'delete'),
    path('update/<int:pk>',views.update,name='update'),
    path('add/',views.add,name='add'),
    path('addroom/',views.addRoom,name='addroom'),
    path('deleteroom/<int:pk>',views.deleteRoom,name='deleteroom')
]