import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from .models import Films, Peoples
from .serializers import FilmSerializer, PeopleSerializer
from .utils import Utils

utils = Utils()
apiclient = APIClient()


class GetGhibleDataTest(TestCase):
    def setUp(self):
        self.valid_film_url = "https://ghibliapi.herokuapp.com/films"
        self.invalid_film_url = "https://ghibliapi.herokuapp.com/films_invalid"
        self.valid_people_url = "https://ghibliapi.herokuapp.com/people"
        self.invalid_people_url = "https://ghibliapi.herokuapp.com/people_invalid"

    def test_valid_url(self):
        response = utils.UpdateGhibli(
            self.valid_film_url, self.valid_people_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_url(self):
        response = utils.UpdateGhibli(
            self.invalid_film_url, self.invalid_people_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_url_load(self):
        response = utils.UpdateGhibli(
            self.valid_film_url, self.valid_people_url)
        response_load = utils.UpdateGhibli(
            self.valid_film_url, self.valid_people_url)
        self.assertEqual(response_load.status_code, status.HTTP_200_OK)

    def test_get_all_films(self):
        response = apiclient.get('/api/films/')
        films = Films.objects.all()
        serializer = FilmSerializer(films, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_poeples(self):
        response = apiclient.get('/api/peoples/')
        pepoles = Peoples.objects.all()
        serializer = PeopleSerializer(pepoles, many=True)
        self.assertEqual(response.data, serializer.data)


class UtilsUnitTests(TestCase):
    def setUp(self):
        self.valid_film_payload = [{
            "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "peoples": [],
            "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Sky",
            "description": "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
            "director": "Hayao Miyazaki",
            "producer": "Isao Takahata",
            "release_date": "1986",
            "rt_score": "95",
            "species": '["https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"]',
            "locations": '["https://ghibliapi.herokuapp.com/locations/"]',
            "vehicles": '["https://ghibliapi.herokuapp.com/vehicles/"]'
        }]
        self.valid_film_payload_update = [{
            "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "peoples": [],
            "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Skyy",
            "description": "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
            "director": "Hayao Miyazaki",
            "producer": "Isao Takahata",
            "release_date": "1986",
            "rt_score": "95",
            "species": '["https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"]',
            "locations": '["https://ghibliapi.herokuapp.com/locations/"]',
            "vehicles": '["https://ghibliapi.herokuapp.com/vehicles/"]',
        }]
        self.valid_people_payload = [{
            "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
            "name": "Lusheeta Toel Ul Laputaaa",
            "gender": "Female",
            "age": "13",
            "eye_color": "Black",
            "hair_color": "Black",
            "films": [
                "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
            ],
            "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
            "url": "https://ghibliapi.herokuapp.com/people/598f7048-74ff-41e0-92ef-87dc1ad980a9"
        }]
        self.valid_people_payload_update = [{
            "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
            "name": "Lusheeta Toel Ul Laputa",
            "gender": "Female",
            "age": "13",
            "eye_color": "Black",
            "hair_color": "Black",
            "films": [
                "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
            ],
            "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
            "url": "https://ghibliapi.herokuapp.com/people/598f7048-74ff-41e0-92ef-87dc1ad980a9"
        }]
        self.valid_people_payload_invalid_film = [{
            "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
            "name": "Lusheeta Toel Ul Laputaaa",
            "gender": "Female",
            "age": "13",
            "eye_color": "Black",
            "hair_color": "Black",
            "films": [],
            "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
            "url": "https://ghibliapi.herokuapp.com/people/598f7048-74ff-41e0-92ef-87dc1ad980a9"
        }]

    def test_create_films(self):
        utils.CreateUpdateFilms(self.valid_film_payload)
        films = Films.objects.get(url=self.valid_film_payload[0]['url'])
        serializer = FilmSerializer(films, many=False)
        self.assertEqual(self.valid_film_payload[0], serializer.data)

    def test_create_update_films(self):
        utils.CreateUpdateFilms(self.valid_film_payload)
        utils.CreateUpdateFilms(self.valid_film_payload_update)
        films = Films.objects.get(url=self.valid_film_payload[0]['url'])
        serializer = FilmSerializer(films, many=False)
        self.assertEqual(self.valid_film_payload_update[0], serializer.data)

    def test_create_peoples(self):
        utils.CreateUpdateFilms(self.valid_film_payload)
        utils.CreateUpdatePeople(self.valid_people_payload)
        peoples = Peoples.objects.get(id=self.valid_people_payload[0]['id'])
        serializer = PeopleSerializer(peoples, many=False)
        self.assertEqual(self.valid_people_payload[0], serializer.data)

    def test_create_update_peoples(self):
        utils.CreateUpdateFilms(self.valid_film_payload)
        utils.CreateUpdatePeople(self.valid_people_payload)
        utils.CreateUpdatePeople(self.valid_people_payload_update)
        peoples = Peoples.objects.get(id=self.valid_people_payload[0]['id'])
        serializer = PeopleSerializer(peoples, many=False)
        self.assertEqual(self.valid_people_payload_update[0], serializer.data)

    def test_create_peoples_invalid_film(self):
        utils.CreateUpdatePeople(self.valid_people_payload)
        peoples = Peoples.objects.get(id=self.valid_people_payload[0]['id'])
        serializer = PeopleSerializer(peoples, many=False)
        self.assertEqual(
            self.valid_people_payload_invalid_film[0], serializer.data)
