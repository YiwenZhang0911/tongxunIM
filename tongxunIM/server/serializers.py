from rest_framework import serializers

from server.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('accid', 'name', 'password')
