from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contactperson = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = PhoneNumberField()

    def __str__(self):
        return self.name

    def get_absolute_ulr(self):
        return reverse('clients:list')
