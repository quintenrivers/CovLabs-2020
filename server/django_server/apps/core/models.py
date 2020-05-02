from django.db import models


class Visit(models.Model):
    """
    A class used to represent a visit to a store
    ...

    Attributes
    ----------
    time_in: DateTime
        the datetime a unique device entered a store
    time_out: DateTime
        the datetime a unique device exited a store
    device_id: CharField
        a unique ID representing a device
    """
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    device_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{device_id} Time-in: {time_in} Time-out: {time_out}"
