# -*- coding: utf-8 -*-

import json

from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route
from django.contrib.auth.models import AnonymousUser

from app.account.models import User
from app.api.account.serializers import AccountSerializer


class AccountViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    error = {
        'error': 'email or password incorrect.'
    }

    def create(self, request):
        if isinstance(request.user, AnonymousUser):
            return super(AccountViewSet, self).create(request)

        return self.login(request)

    @list_route(methods=['post'])
    def login(self, request):
        email = request.data.pop("email")
        password = request.data.pop("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(self.error, status=status.HTTP_400_BAD_REQUEST)
