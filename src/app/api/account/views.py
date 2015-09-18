# -*- coding: utf-8 -*-

import json

from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import list_route, detail_route

from app.account.models import User
from app.api.account import serializers
from app.api.podcast.serializers import PodcastSerializer


class AccountViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [AllowAny]
    error = {
        'error': 'email or password incorrect.'
    }

    def get(self, request):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.user, AnonymousUser):
            return super(AccountViewSet, self).create(request)

        return self.login(request)

    @list_route(methods=['post', 'get'])
    def bookmarked_podcasts(self, request):
        if request.method == 'POST':
            serializer = serializers.BookmarkPodcastsSerializer(
                request.user,
                data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        queryset = request.user.bookmarked_podcasts.all()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = PodcastSerializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = PodcastSerializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=['post'])
    def login(self, request):
        email = request.data.pop("email")
        password = request.data.pop("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(self.error, status=status.HTTP_400_BAD_REQUEST)
