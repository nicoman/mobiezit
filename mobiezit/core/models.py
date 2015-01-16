from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    imdb_link = models.URLField(max_length=100, unique=True)
    add_by = models.ForeignKey(User)

    def __str__(self):
        return self.imdb_link


class UserMovie(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
    viewed = models.BooleanField(default=False)


class Recommend(models.Model):
    movie = models.ForeignKey(Movie)
    recommender = models.ForeignKey(User, related_name="user_recommender")
    recommended = models.ForeignKey(User, related_name="user_recommended")


class Followers(models.Model):
    follower = models.ForeignKey(User, related_name="user_follower")
    following = models.ForeignKey(User, related_name="user_following")