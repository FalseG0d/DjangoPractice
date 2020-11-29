from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from Contactus.models import Type as Help_Type

#from Contactus.models import Faq
from Request.models import Order
from Service.models import Parent_Type

from django.contrib.auth.decorators import login_required

from Request.forms import OrderForm
# Create your views here.

def store(request):
    products=Product.objects.all()
    parent_types=Parent_Type.objects.all()

    context={
        'products':products,
        'parent_types':parent_types,
        }
    return render(request,'service/store.html',context)

def all_service(request,pk):
    parent_types=Parent_Type.objects.all()
    parent_type=Parent_Type.objects.get(id=pk)
    type=Type.objects.filter(parent=parent_type)

    product=Product.objects.all()#(type=type)

    context={
        'parent_type':parent_type,
        'types':type,
        'products':product,
        'parent_types':parent_types,
    }

    return render(request,'service/type.html',context)


def service(request,pk):
       
    product=Product.objects.get(id=pk)
    form=OrderForm(initial={'product':product})

    if request.method=='POST':

        if not request.user.is_authenticated:
            return redirect('login')
            
        form=OrderForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            content_form = form.save(commit=False)
            content_form.customer_id = request.user.id
            content_form.status = 'Placed'
            content_form.save()
            return redirect('home')


    testimonial=Testimonial.objects.all()
    count=Order.objects.filter(product=product).count()
    help_type=Help_Type.objects.all()
    parent_types=Parent_Type.objects.all()

    context={
        'product':product,
        'testimonials':testimonial,
        'count':count,
        'types':help_type,
        'form':form,
        'parent_types':parent_types,
        }
    return render(request,'service/service.html',context)