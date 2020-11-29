from django.db import models
from Service.models import Product

# Create your models here.


class Order(models.Model):
    STATUS=(
        ('Placed','Placed'),
        ('Lawyer_Assigned','Lawyer Assigned'),
        ('Working','Working'),
        ('Complete','Complete'),
    )
    customer_id=models.CharField(max_length=200)
    date_ordered=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS,default=STATUS[0][0])

    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    requirenment = models.FileField(upload_to='documents',null=True)

    def __str__(self):
        return str(self.product)

