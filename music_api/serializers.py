from rest_framework import serializers

from .models import Musician, Album, Track


class MusicianSerializers(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
