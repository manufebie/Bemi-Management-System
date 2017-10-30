from django.db import models
from django.urls import reverse

from .validators import validate_mime_type


class Document(models.Model):
    document = models.FileField(validators=[validate_mime_type],
                                upload_to='docs')
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('documents:list')