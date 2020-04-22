from django.contrib import admin
from . import models


class VisitAdmin(admin.ModelAdmin):
    fields = ['time_in', 'time_out', 'device_id']


admin.site.register(models.Visit, VisitAdmin)
