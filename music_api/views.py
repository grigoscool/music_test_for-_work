from rest_framework import generics
from rest_framework import permissions
from .models import Musician, Album, Track
from .serializers import (
    MusicianSerializers,
    AlbumSerializers,
    TrackSerializers
)

from .permissions import IsAdminOrReadOnly

class MusicianListApiView(generics.ListAPIView):
    """
    List of musicians.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumListApiView(generics.ListAPIView):
    """
    List of albums.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrackListApiView(generics.ListAPIView):
    """
    List of tracks.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MusicianRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    Musician CRUD.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers


class AlbumCreationApiView(generics.CreateAPIView):
    """
    Creation of Album.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers


class TrackDeleteApiView(generics.DestroyAPIView):
    """
    Delete track for admin, and read only for everybody.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializers
    permission_classes = [IsAdminOrReadOnly]