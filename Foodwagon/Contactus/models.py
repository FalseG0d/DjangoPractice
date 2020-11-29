from django.db import models

# Create your models here.
class Email(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    number=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    body=models.TextField()
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Help(models.Model):
    topic=models.CharField(max_length=100)
    body=models.TextField()
    type_of=models.ForeignKey(Type,on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.topic