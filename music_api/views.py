from rest_framework import generics

from .models import Musician, Album, Track
from .serializers import MusicianSerializers


class MusicianListApiView(generics.ListAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializers
