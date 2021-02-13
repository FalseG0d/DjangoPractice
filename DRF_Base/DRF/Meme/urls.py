from django.urls import path
from . import views

urlpatterns = [
    path('api/Meme/', views.MemeListCreate.as_view() ),
]