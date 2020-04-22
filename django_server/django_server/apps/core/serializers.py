from rest_framework import serializers
from . import models


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visit
        fields = ('device_id', 'time_in', 'time_out')
