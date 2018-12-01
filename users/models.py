from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    teacherID = models.CharField(max_length=10, blank=True)
    designations = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile-picture/')

    def __str__(self):
        return self.username
