from django.contrib.auth.models import User
from django.db import models
from django.http import request
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    biography = models.TextField()
    contacts = models.CharField(max_length=200)
    # ip_address = models.GenericIPAddressField(default=None)
    history = HistoricalRecords()

    def __str__(self):
        data = '{0.first_name} {0.last_name}'
        return data.format(self)


class RequestInformation(models.Model):
    request_method = models.CharField(max_length=20, blank=True, null=True)
    execution_time = models.DateTimeField(blank=True, null=True)


