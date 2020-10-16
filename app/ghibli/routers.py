from rest_framework import routers
from .viewsets import FilmViewSet, PeopleViewSet


router = routers.DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'peoples', PeopleViewSet)
