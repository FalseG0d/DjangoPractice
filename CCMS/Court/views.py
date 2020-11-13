from django.shortcuts import render
from .models import Court
# Create your views here.
def index(request):
    courts=Court.objects.all()
    return render(request,"index.html",{'courts':courts})