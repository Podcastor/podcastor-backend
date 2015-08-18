# -*- coding: utf-8 -*-

import django_filters

from app.podcast.models import Episode, Podcast


class EpisodeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_type='icontains')
    description = django_filters.CharFilter(lookup_type='icontains')
    slug = django_filters.CharFilter(lookup_type='icontains')
    podcast__title = django_filters.CharFilter(lookup_type='icontains')
    podcast__slug = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Episode
        fields = ['title', 'description', 'slug', 'pub_date', 'podcast__title',
                  'podcast__slug', 'podcast__id']
