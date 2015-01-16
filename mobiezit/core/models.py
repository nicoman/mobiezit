from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    imdb_link = models.URLField(max_length=100, unique=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.imdb_link


class UserMovie(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    viewed = models.BooleanField(default=False)