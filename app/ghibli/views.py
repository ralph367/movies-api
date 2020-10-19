from django.shortcuts import render
from .viewsets import FilmViewSet
from rest_framework.views import APIView
import requests


class MovieView(APIView):
    template_name = 'movies.html'

    def get(self, request):
        films_response = requests.get("http://127.0.0.1:8000/api/films/")
        film_list = films_response.json()
        return render(request, self.template_name, {'movies': film_list})
