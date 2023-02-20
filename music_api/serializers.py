from rest_framework import serializers

from .models import Musician, Album, Track


class MusicianSerializers(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'
