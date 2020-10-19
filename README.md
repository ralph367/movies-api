# Movies API
 
This is a repository for a movie list api task where Django will make a get requests on 2 external API, add the required data as a Django model in order to make a relation between these 2 requests
## Disclaimer this is just a simple example for testing and developing not for production use

## Prerequistes 

Tested on:
- Windows 10
- Python 3.8

## Installation

Running the followin application requires:
- Clonning the repository
- Installing requirements.txt file
- Running the server

In order to install the aforementioned requirement run the following commands in your terminal
```sh
pip install -r requirements.txt
```

Once done change your directory to the app folder in this repository and run:
```sh
python manage.py runserver
```

Then just access the following address to get a plain list of the movies and characters : http://127.0.0.1:8000/movies/

## Documentation

### Django

In the following system django is only being used to save Ghibli data, these actions will be triggered using API by the help of Django REST Framework
| Methods | URLs              | Actions                       |
|---------|-------------------|-------------------------------|
| GET     | /api/films/       | get all available films       |
| GET     | /api/peoples/     | get all the available people  |

When calling one of the above functions, Util class will be triggered in order to get data from Ghibli API server and create every record in our database. Since film and people models got a many to many relation then when we get all the available films it is going to contain peoples field.
Also to prevent calling the external api on every page load I made it that if no one accessed the page from the last minute it call again the external API else it is only going to get the data available in our database.

### Test-driven Development

I tried using unit tests for every function byt maybe I didn't try all the available and possible cases for each function so maybe I missed some of the special cases. The idea behind using TDD was just to make sure after each function update/changes the system will remain working without any error/bug.
