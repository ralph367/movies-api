from django.db import models

class Films(models.Model):
    id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=200, default=None)
    director = models.CharField(max_length=200, default=None)
    producer = models.CharField(max_length=200, default=None)
    release_date = models.CharField(max_length=200, default=None)
    rt_score = models.CharField(max_length=200, default=None)
    people = models.CharField(max_length=200, default=None)
    species = models.CharField(max_length=200, default=None)
    locations = models.CharField(max_length=200, default=None)
    vehicles = models.CharField(max_length=200, default=None)
    url = models.CharField(max_length=200, default=None, primary_key=True)


class Peoples(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=200, blank=True)
    eye_color = models.CharField(max_length=200, blank=True)
    hair_color = models.CharField(max_length=200, blank=True)
    films = models.ManyToManyField(Films, related_name="peoples", blank=True)
    species = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
