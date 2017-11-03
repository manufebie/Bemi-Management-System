from django.db import models
from django.conf import settings
from django.urls import reverse

from projects.models import Project


class Task(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255,  null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    obstacles = models.CharField(max_length=255, blank=True,  null=True)

    active = models.BooleanField(default=True, blank=True)

    deadline = models.DateField(blank=True, null=True, help_text='Set a deadline for your task')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:list')