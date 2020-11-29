from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from Service.models import *
from .models import *
from Request.models import Order

from .forms import CreateUserForm
#from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

def error404(request,exception):
    parent_types=Parent_Type.objects.all()
    context={
        'parent_types':parent_types,
    }
    return render(request,'home/404.html',context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def register(request):
    parent_types=Parent_Type.objects.all()
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'parent_types':parent_types,
        'form':form
    }
    return render(request,'home/register.html',context)

@unauthenticated_user
def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            return HttpResponse('Username or Password Incorrect')
    parent_types=Parent_Type.objects.all()
    context={
        'parent_types':parent_types,
    }
    return render(request,'home/login.html',context)
    

def home(request):

    #register=UserCreationForm()
    
    services=Product.objects.all()
    types=Type.objects.all()
    reviews=Review.objects.all()
    count=Order.objects.count()
    helpers=Helper.objects.all()
    helps=Help.objects.all()
    talkers=Talker.objects.all()
    parent_types=Parent_Type.objects.all()

    context={
        'services':services,
        'types':types,
        'reviews':reviews,
        'count':count,
        'helpers':helpers,
        'helps':helps,
        'talkers':talkers,
        'parent_types':parent_types,
    }

    return render(request,'home/index.html',context)
