from django.db import models

# Create your models here.
class Slider(models.Model):
    image=models.ImageField(upload_to='images/slider')
    name=models.CharField(max_length=20)
    first=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image=models.ImageField(upload_to='images/portfolio')
    name=models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self):
        return self.name

class About(models.Model):
    logo=models.ImageField(upload_to='images')
    name=models.CharField(max_length=50)
    desc=models.TextField()
    #color=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RecentImage(models.Model):
    image=models.ImageField(upload_to='images/recent')
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Link(models.Model):
    name=models.CharField(max_length=20)
    
    ICON=(
        ('fa fa-facebook','Facebook'),
        ('fa fa-twitter','Twitter'),
        ('fa fa-linkedin','LinkedIn'),
        ('fa fa-pintrest','Pintrest'),
        ('fa fa-snapchat','Snapchat'),
        ('fa fa-youtube','Youtube'),
        ('fa fa-reddit-alien','Reddit'),
        ('fa fa-medium','Medium'),
        ('fa fa-google-plus','Google Plus'),
        ('fa fa-js-fiddle','Fiddle'),
        ('fa fa-github','Github'),
    )
    icon=models.CharField(max_length=120,choices=ICON,default=ICON[0][0])
    link=models.CharField(max_length=200)

    def __str__(self):
        return self.name