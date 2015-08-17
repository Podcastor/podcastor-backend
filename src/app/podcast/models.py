# -*- coding: utf-8 -*-

import requests
import xmltodict

from django.db import models
from django.utils.text import slugify


class Podcast(models.Model):
    title = models.CharField(max_length="255")
    description = models.TextField()
    link = models.URLField()
    slug = models.SlugField()
    image = models.URLField(null=True, blank=True)

    @classmethod
    def get_data_from_feed(self, feed_url):
        response = requests.get(feed_url)

        if response.status_code == 200:
            data = xmltodict.parse(response.content)['rss']['channel']

            return {
                'title': data['title'],
                'description': data['description'],
                'link': feed_url,
                'image': data['image']['url']
            }

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Podcast, self).save(*args, **kwargs)


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    audio_link = models.URLField()
    link = models.URLField()
    image = models.URLField()
    pub_date = models.DateTimeField()
