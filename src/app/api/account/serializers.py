# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from app.account.models import User
from app.podcast.models import Podcast


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class AccountSerializer(serializers.ModelSerializer):
    auth_token = TokenSerializer(required=False)
    bookmarked_podcasts = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True)

    class Meta:
        model = User
        read_only_fields = ['bookmarked_podcasts']

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)

        return user

    def to_representation(self, obj):
        data = super(AccountSerializer, self).to_representation(obj)
        data.pop("password")

        return data


class BookmarkPodcastsSerializer(serializers.ModelSerializer):
    bookmarked_podcasts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Podcast.objects.all())

    class Meta:
        model = User
        fields = ['bookmarked_podcasts']
