from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header="DarkLight Photography"
admin.site.site_title="DarkLight Photography"

admin.site.unregister(Group)

# Register your models here.
admin.site.register(Slider)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(RecentImage)
admin.site.register(Link)