from rest_framework import viewsets
from . import models
from . import serializers


class VisitViewSet(viewsets.ModelViewSet):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer

