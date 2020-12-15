from django.db import models

# Create your models here.
class NewsType(models.Model):
    sect = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s" % (self.sect)

class News(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    desc=models.TextField()
    image=models.ImageField(upload_to='pics')
    sect = models.ForeignKey(NewsType, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class OtherType(models.Model):
    sect = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s" % (self.sect)

class Other(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    desc=models.TextField()
    image=models.ImageField(upload_to='pics')
    sect = models.ForeignKey(OtherType, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']