from rest_framework import generics

from .models import Musician, Album, Track
from .serializers import (
    MusicianSerializers,
    AlbumSerializers,
    TrackSerializers
)


class MusicianListApiView(generics.ListAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers


class AlbumListApiView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers


class TrackListApiView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializers


class MusicianRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers


class AlbumCreationApiView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers