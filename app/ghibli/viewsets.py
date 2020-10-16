from rest_framework import viewsets
from .models import Films, Peoples
from .serializers import FilmSerializer, PeopleSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeopleSerializer
