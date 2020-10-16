from .models import Films, Peoples
from rest_framework import serializers


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peoples
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    peoples = PeopleSerializer(read_only=True, many=True)

    class Meta:
        model = Films
        fields = '__all__'
