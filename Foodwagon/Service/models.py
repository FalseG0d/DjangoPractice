from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parent_Type(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)

    def __str__(self):
        return self.name

class Type(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    first=models.BooleanField()

    parent=models.ForeignKey(Parent_Type,null=True,on_delete=models.SET_NULL,blank=False)
    visible=models.BooleanField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    image=models.ImageField(null=True,blank=True,upload_to='product_images')

    description=models.TextField(null=True)
    instruction=models.TextField(null=True)
    requirenment = models.FileField(upload_to='requirements',null=True)

    visible=models.BooleanField()

    type=models.ForeignKey(Type,null=True,on_delete=models.SET_NULL,blank=False)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Testimonial(models.Model):
    author=models.CharField(max_length=70)
    company=models.CharField(max_length=70)
    body=models.TextField(null=True)

    image=models.ImageField(null=True,blank=True,upload_to='testimonial_images')

    def __str__(self):
        return str(self.author+":"+self.company)