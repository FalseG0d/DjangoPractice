from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header="Legal24By7"
admin.site.site_title="Legal24By7"

#admin.site.register(Lawyer)
#admin.site.register(Type)
#admin.site.register(Service)
#admin.site.register(Request)
admin.site.register(Review)
admin.site.register(Help)
admin.site.register(Helper)
admin.site.register(Talker)