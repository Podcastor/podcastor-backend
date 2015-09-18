# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = self.model(**kwargs)

        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    bookmarked_podcasts = models.ManyToManyField('podcast.Podcast')
    bookmarked_episodes = models.ManyToManyField('podcast.Episode')

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return '{0}'.format(self.first_name)
