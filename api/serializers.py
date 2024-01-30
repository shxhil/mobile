from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Phonemodel


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=["id","username","email","password"]


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phonemodel
        fields="__all__"