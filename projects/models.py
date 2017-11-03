from django.db import models
from django.conf import settings
from django.urls import reverse

from clients.models import Company

class Division(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=120, null=True)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL)
    division = models.ForeignKey(Division)
    client = models.ForeignKey(Company)
    description = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:list')
