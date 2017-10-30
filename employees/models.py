from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from django.urls import reverse


class EmployeeManager(BaseUserManager):
    def create_user(self, firstname, lastname, job_title, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            firstname = firstname,
            lastname = lastname,
            job_title = job_title,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, job_title, email, password):
        user = self.create_user(
            firstname,
            lastname,
            job_title,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    cover_image = models.ImageField(upload_to='media', blank=True, null=True)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    job_title = models.CharField(max_length=120)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'job_title']

    def get_full_name(self):
        # The user is identified by their firstname
        return self.firstname

    def get_short_name(self):
        # The user is identified by their firstname
        return self.firstname

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_absolute_url(self):
        return reverse('login')
        

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin