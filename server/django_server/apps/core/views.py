from rest_framework import viewsets
from django_filters import rest_framework as filters
from . import models
from . import serializers


class VisitFilterSet(filters.FilterSet):
    class Meta:
        model = models.Visit
        fields = {
            'time_in': [
                'exact',
                'contains',

                # year
                'year',
                'year__gt',
                'year__lt',

                # month
                'month',
                'month__gt',
                'month__lt',

                # day
                'day',
                'day__gt',
                'day__lt',

                # hour
                'hour',
                'hour__gt',
                'hour__lt',

                # minute
                'minute',
                'minute__gt',
                'minute__lt',
            ],
            'time_out': ['exact', 'contains'],
            'device_id': ['exact', 'contains']
        }


class VisitViewSet(viewsets.ModelViewSet):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer
    filterset_class = VisitFilterSet
