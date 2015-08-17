# -*- coding: utf-8 -*-

import json

from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from app.podcast.models import Podcast, Episode
from app.api.podcast.serializers import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    permissions_class = [IsAuthenticated]
    serializer_class = PodcastSerializer

    @list_route(methods=['get'])
    def search(self, request):
        qs = Podcast.objects.filter(
            Q(title__icontains=request.query_params.get('title') or '') |
            Q(link__icontains=request.query_params.get('link') or ''))

        if qs:
            page = self.paginate_queryset(qs)
            serializer = self.serializer_class(page, many=True)

            return self.get_paginated_response(serializer.data)

        data = Podcast.get_data_from_feed(request.query_params.get('link'))

        if data:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'detail': 'Feed URL is invalid or non exists.'},
                        status=HTTP_400_BAD_REQUEST)
