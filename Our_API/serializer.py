from django.contrib.auth.models import Group
from django.conf import settings
from Boroughs.models import Borough, Photo
from users.models import CustomUser as User
from rest_framework import serializers


class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borough
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
