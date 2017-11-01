from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from tasks.models import Task
from projects.models import Project

class Comment(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    #task = models.ForeignKey(Task)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.firstname