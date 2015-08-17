# -*- coding: utf-8 -*-

import requests
import xmltodict

from django.db import models
from django.utils.text import slugify

from app.podcast import tasks


class Podcast(models.Model):
    title = models.CharField(max_length="255")
    description = models.TextField()
    link = models.URLField(max_length=120)
    slug = models.SlugField(max_length=120)
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

    def get_feed_data(self):
        response = requests.get(self.link)

        if response.status_code == 200:
            return xmltodict.parse(response.content)['rss']['channel']

    def save(self, *args, **kwargs):
        is_new = False if self.id else True
        self.slug = slugify(self.title)

        super(Podcast, self).save(*args, **kwargs)

        if is_new:
            tasks.create_episodes_from_podcast.delay(self.id)


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=120)
    audio_link = models.URLField(max_length=120)
    link = models.URLField(max_length=120)
    image = models.URLField(null=True, blank=True)
    pub_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Episode, self).save(*args, **kwargs)
