from .models import Peoples, Films
from datetime import datetime, timedelta
import requests

class Utils:
    last_updated_time = datetime(2013,12,30,23,59,59)   
    films_response_json = []
    peoples_response_json = []

    def UpdateGhibli(self):
        if ( datetime.now() - self.last_updated_time ).total_seconds() > 60:
            print("Updating Ghibli")
            try:
                films_url = "https://ghibliapi.herokuapp.com/films"
                films_response = requests.get(films_url)
            except requests.exceptions.RequestException as e:
                print(e)
                
            try:
                people_url = "https://ghibliapi.herokuapp.com/people"
                people_response = requests.get(people_url)
            except requests.exceptions.RequestException as e:
                print(e)

            if (films_response.status_code == 200 and people_response.status_code == 200):
                self.peoples_response_json = people_response.json()
                self.CreateUpdatePeople()
                self.films_response_json = films_response.json()
                self.CreateUpdateFilms()
                self.last_updated_time = datetime.now()
        else:
            return
            
    def CreateUpdateFilms(self):
        for data in self.films_response_json:
            Films.objects.update_or_create(
                id=data["id"],
                title=data["title"],
                description=data["description"],
                director=data["director"],
                producer=data["producer"],
                release_date=data["release_date"],
                rt_score=data["rt_score"],
                species=data["species"],
                locations=data["locations"],
                vehicles=data["vehicles"],
                url=data["url"]
            )
        
    def CreateUpdatePeople(self):
        for data in self.peoples_response_json:
            person, created = Peoples.objects.update_or_create(
                id=data["id"],
                name=data["name"],
                gender=data["gender"],
                age=data["age"],
                eye_color=data["eye_color"],
                hair_color=data["hair_color"],
                species=data["species"],
                url=data["url"]
            )
            if not created:
                person.films.clear()
            for film in data["films"]:
                film = Films.objects.get(url=film)
                person.films.add(film)
