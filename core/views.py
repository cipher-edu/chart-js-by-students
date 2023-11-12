from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    davlat = Strana.objects.all()
    return render(request, 'index.html',{'davlat':davlat})