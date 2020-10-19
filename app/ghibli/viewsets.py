from rest_framework import viewsets
from .models import Films, Peoples
from .serializers import FilmSerializer, PeopleSerializer
from rest_framework.response import Response
from .utils import Utils

utils = Utils()


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer
    film_url = "https://ghibliapi.herokuapp.com/films"
    people_url = "https://ghibliapi.herokuapp.com/people"

    def list(self, request):
        utils.UpdateGhibli(self.film_url, self.people_url)
        serializer = FilmSerializer(self.queryset, many=True)
        return Response(serializer.data)


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeopleSerializer
    film_url = "https://ghibliapi.herokuapp.com/films"
    people_url = "https://ghibliapi.herokuapp.com/people"

    def list(self, request):
        utils.UpdateGhibli(self.film_url, self.people_url)
        serializer = PeopleSerializer(self.queryset, many=True)
        return Response(serializer.data)
