from rest_framework import generics
from applications.music.models import Music
from applications.music.serializers import MusicSerializer


class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

