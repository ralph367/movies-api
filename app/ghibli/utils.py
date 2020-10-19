from .models import Peoples, Films
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
import requests
import time


class Utils:
    last_updated_time = datetime(2013, 12, 30, 23, 59, 59)

    def UpdateGhibli(self, films_url, people_url):
        if (datetime.now() - self.last_updated_time).total_seconds() > 60:
            try:
                films_response = requests.get(films_url)
            except requests.exceptions.RequestException as e:
                print(e)

            try:
                people_response = requests.get(people_url)
            except requests.exceptions.RequestException as e:
                print(e)

            if (films_response.status_code == 200 and
                    people_response.status_code == 200):
                self.CreateUpdateFilms(films_response.json())
                self.CreateUpdatePeople(people_response.json())
                self.last_updated_time = datetime.now()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_200_OK)

    def CreateUpdateFilms(self, json_data):
        for data in json_data:
            film, created = Films.objects.update_or_create(
                id=data["id"],
                url=data["url"],
                defaults={
                    'title': data["title"],
                    'description': data["description"],
                    'director': data["director"],
                    'producer': data["producer"],
                    'release_date': data["release_date"],
                    'rt_score': data["rt_score"],
                    'species': data["species"],
                    'locations': data["locations"],
                    'vehicles': data["vehicles"],
                }
            )

    def CreateUpdatePeople(self, json_data):
        for data in json_data:
            person, created = Peoples.objects.update_or_create(
                id=data["id"],
                defaults={
                    'name': data["name"],
                    'gender': data["gender"],
                    'age': data["age"],
                    'eye_color': data["eye_color"],
                    'hair_color': data["hair_color"],
                    'species': data["species"],
                    'url': data["url"],
                }
            )
            if not created:
                person.films.clear()
            for film in data["films"]:
                try:
                    film = Films.objects.get(url=film)
                except Films.DoesNotExist:
                    film = None
                person.films.add(film)
