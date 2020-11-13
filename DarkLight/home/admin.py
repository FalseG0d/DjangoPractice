from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User

admin.site.site_header="DarkLight Photography"
admin.site.site_title="DarkLight Photography"

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(Slider)
admin.site.register(GalleryImage)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Link)