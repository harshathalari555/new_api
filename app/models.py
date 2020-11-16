from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.movie_name


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username


