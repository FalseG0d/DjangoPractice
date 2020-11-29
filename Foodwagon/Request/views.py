from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Order
from Service.models import Parent_Type
# Create your views here.

@login_required(login_url='login')
def cart(request):
    parent_types=Parent_Type.objects.all()
    orders=Order.objects.all().filter(customer_id=request.user.id)

    context={
        'parent_types':parent_types,
        'orders':orders,
    }
    return render(request,"request/cart.html",context)