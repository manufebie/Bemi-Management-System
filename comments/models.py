from django.db import models
from django.conf import settings

from tasks.models import Task
from projects.models import Project

class Comment(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    task = models.ForeignKey(Task)
    # project = models.ForeignKey(Project, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.firstname