from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=120)
    date_created=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=200, null=True)
    profile_pic=models.ImageField(null=True,blank=True,default="default.png")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name=models.CharField(max_length=120)
    price=models.FloatField()
    category=models.CharField(max_length=120,choices=CATEGORY)
    description=models.CharField(max_length=120)
    date_created=models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=datetime.now()+timedelta(days=7))
    status=models.CharField(max_length=120,choices=STATUS,default=STATUS[0][0])
    note=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.product.name