from rest_framework import viewsets
from .serializers import PersonSerializer
from .. import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer