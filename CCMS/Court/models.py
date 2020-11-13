from django.db import models

# Create your models here.
class Court(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(max_length=100)
    loc=models.CharField(max_length=30)
    fast=models.BooleanField(default=False)

class Cases(models.Model):
    code=models.CharField(max_length=15)
    lasthearing=models.DateField()
    status=models.CharField(max_length=10)
    desc=models.TextField()