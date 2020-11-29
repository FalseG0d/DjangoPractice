from django.contrib import admin

# Register your models here.
from . models import *

#admin.site.register(Customer)
#admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Parent_Type)
admin.site.register(Type)
admin.site.register(Testimonial)
#admin.site.register(OrderItem)
#admin.site.register(Active_Customer)