# -*- coding: utf-8 -*-

import json

from django.db.models import Q
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from app.podcast import filters
from app.podcast.models import Podcast, Episode
from app.api.podcast.serializers import PodcastSerializer, EpisodeSerializer


class EpisodeViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
    filter_class = filters.EpisodeFilter


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    filter_class = filters.PodcastFilter

    @list_route(methods=['post'])
    def create_from_feed(self, request):
        data = Podcast.get_data_from_feed(request.data.get('link'))

        if data:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'detail': 'Feed URL is invalid or non exists.'},
                        status=status.HTTP_400_BAD_REQUEST)
