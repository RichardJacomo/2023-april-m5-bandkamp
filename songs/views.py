from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(album=Album.objects.get(pk=self.kwargs['pk']))