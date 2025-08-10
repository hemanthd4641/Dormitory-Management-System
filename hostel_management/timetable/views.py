from django.shortcuts import render,redirect,get_object_or_404
from .models import FoodTimetable
from .forms import TimeTableForm
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def viewTimetable(request):
    timetable = FoodTimetable.objects.all()
    context = {'timetable':timetable, 'user': request.user}
    return render(request,'timetable.html',context)

@login_required
def update_timetable_view(request, pk):
    timetable = get_object_or_404(FoodTimetable, pk = pk)

    if request.method == 'POST':
        form = TimeTableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('timetable:Foodtimetable') 
    else:
        form = TimeTableForm(instance=timetable)

    return render(request, 'update_timetable.html', {'form': form, 'timetable': timetable, 'user': request.user})





    