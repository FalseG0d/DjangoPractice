from django.contrib import admin
from .models import News,NewsType,Other,OtherType
# Register your models here.
admin.site.register(News)
admin.site.register(NewsType)
admin.site.register(OtherType)
admin.site.register(Other)

admin.site.site_header="Disease Reporter"