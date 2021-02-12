from rest_framework import serializers

from .models import Meme


class MemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meme
        fields = ('name', 'image', 'pub_date', 'credit')
