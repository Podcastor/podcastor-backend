# -*- coding: utf-8 -*-

from django.utils.text import slugify
from rest_framework import serializers

from app.podcast.models import Podcast, Episode


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'slug', 'title', 'description', 'link', 'image']
        read_only_fields = ('id', 'slug')

    def create(self, validated_data):
        slug = slugify(validated_data['title'])

        try:
            return Podcast.objects.get(slug=slug)
        except Podcast.DoesNotExist:
            validated_data['slug'] = slug

            return super(PodcastSerializer, self).create(validated_data)


class EpisodeSerializer(serializers.ModelSerializer):
    podcast = PodcastSerializer()

    class Meta:
        model = Episode
        fields = ['id', 'podcast', 'title', 'description', 'slug',
                  'audio_link', 'link', 'image', 'pub_date']
