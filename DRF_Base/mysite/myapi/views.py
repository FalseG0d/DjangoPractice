from rest_framework import viewsets

from .serializers import MemeSerializer
from .models import Meme


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all().order_by('name')[:100]
    serializer_class = MemeSerializer