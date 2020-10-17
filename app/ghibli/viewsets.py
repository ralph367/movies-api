from rest_framework import viewsets
from .models import Films, Peoples
from .serializers import FilmSerializer, PeopleSerializer
from rest_framework.response import Response
from .utils import Utils

utils = Utils()

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeopleSerializer

    def list(self, request):
        utils.UpdateGhibli()
        queryset = Peoples.objects.all()
        serializer = PeopleSerializer(queryset, many=True)
        return Response(serializer.data)