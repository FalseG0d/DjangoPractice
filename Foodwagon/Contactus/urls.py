from django.urls import path
from . import views

urlpatterns = [
    path('',views.email,name="email"),
    path('help',views.help,name="help")
]
