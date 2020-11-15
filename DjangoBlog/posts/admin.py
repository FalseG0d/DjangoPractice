from django.contrib import admin

from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","timestamp","update","draft","publish"]
    list_filter=["update","timestamp"]
    list_editable = ["draft","publish"]
    search_fields=["title","content"]
    class Meta:
        model=Post

admin.site.register(Post,PostModelAdmin)
