# -*- coding: utf-8 -*-

from django.db import models


class Podcast(models.Model):
    title = models.CharField(max_length="255")
    description = models.TextField()
    link = models.URLField()
    slug = models.SlugField()


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    audio_link = models.URLField()
    link = models.URLField()
    image = models.URLField()
    pub_date = models.DateTimeField()
