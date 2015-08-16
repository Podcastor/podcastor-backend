# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from app.account.models import User


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class AccountSerializer(serializers.ModelSerializer):
    auth_token = TokenSerializer(required=False)

    class Meta:
        model = User

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)

        return user

    def to_representation(self, obj):
        data = super(AccountSerializer, self).to_representation(obj)
        data.pop("password")

        return data
