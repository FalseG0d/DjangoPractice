from django.shortcuts import render
from .models import Meme
from .serializers import MemeSerializer
from rest_framework import generics

# Create your views here.

class MemeListCreate(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
