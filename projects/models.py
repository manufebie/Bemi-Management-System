from django.db import models
from django.conf import settings
from django.urls import reverse

from clients.models import Company


class Project(models.Model):
    PUMPS = 'Pumps'
    PIPES = 'Pipes'
    POWER_BANKS = 'Power Banks'
    DIVISION_CHOICES = (
        (PUMPS, 'Pumps'),
        (PIPES, 'Pipes'),
        (POWER_BANKS, 'Power Banks')
    )
    name = models.CharField(max_length=120, null=True)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL)
    division = models.CharField(max_length=25, choices=DIVISION_CHOICES, default=PUMPS)
    client = models.ForeignKey(Company, blank=True)
    description = models.CharField(max_length=120)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:list')
