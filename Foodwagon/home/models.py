from django.db import models

# Create your models here.

class Review(models.Model):
    subject=models.CharField(max_length=120,null=False)
    body=models.CharField(max_length=500,null=False)
    author=models.CharField(max_length=120,null=False)
    first=models.BooleanField()
    
    def __str__(self):
        return self.subject

class Help(models.Model):
    type=models.CharField(max_length=120,null=False,blank=False)
    first=models.BooleanField()

    def __str__(self):
        return self.type

class Helper(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    image=models.ImageField(null=False)
    desc=models.CharField(max_length=500,null=False,blank=False)
    
    type=models.ForeignKey(Help,null=True,on_delete=models.SET_NULL,blank=False)
    def __str__(self):
        return self.name

class Talker(models.Model):
    name=models.CharField(max_length=120,null=False,blank=False)
    image=models.ImageField(null=False)
    link=models.CharField(max_length=500,null=False,blank=False)

    def __str__(self):
        return self.name