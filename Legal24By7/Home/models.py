from django.db import models

# Create your models here.

class Lawyer(models.Model):
    name=models.CharField(max_length=200, null=False, blank=False)
    email=models.CharField(max_length=200, null=False, blank=False)
    phone=models.CharField(max_length=12, null=False, blank=False)
    rating=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=500, null=False, blank=False)
    documents= models.FileField(upload_to='credentials/', null=False, blank=False)

    def __str__(self):
        return self.name


class Type(models.Model):
    name=models.CharField(max_length=120,null=False)
    
    def __str__(self):
        return self.name

    

class Service(models.Model):
    name=models.CharField(max_length=120,null=False)
    details=models.CharField(max_length=500,null=False)
    cost=models.IntegerField()
    tag=models.CharField(max_length=120,null=True)
    type=models.ManyToManyField(Type)
    
    def __str__(self):
        return self.name


class Review(models.Model):
    subject=models.CharField(max_length=120,null=False)
    body=models.CharField(max_length=500,null=False)
    #author=models.ForeignKey(Customer,null=True)
    
    def __str__(self):
        return self.subject

class Request(models.Model):
    client=models.CharField(max_length=120,null=False,blank=False)

    name=models.CharField(max_length=120,null=False,blank=False)
    details=models.CharField(max_length=500,null=False,blank=False)
    service=models.ForeignKey(Service,null=True,on_delete=models.SET_NULL,blank=False)
    
    lawyer=models.ForeignKey(Lawyer,null=True,on_delete=models.SET_NULL,blank=False)
    documents= models.FileField(upload_to='credentials/', null=False, blank=False)
    date_created=models.DateTimeField(auto_now_add=True,null=False)
    
    def __str__(self):
        return self.name
