from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def Home(request):

    services=Service.objects.all()
    types=Type.objects.all()
    reviews=Review.objects.all()
    count=Request.objects.count()
    return render(request,"Home/dashboard.html",{'services':services,'types':types,'reviews':reviews,'count':count})