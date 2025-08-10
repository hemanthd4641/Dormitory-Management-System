from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
# Create your views here.
def index(request):
    querry = request.GET.get('q') if(request.GET.get('q')!=None) else ''
    users = User.objects.filter(Q(username__icontains=querry))
    context = {'users':users,'querry':querry}
    return render(request,'profile.html',context)