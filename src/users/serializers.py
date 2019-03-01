from rest_framework import serializers

from .models import User


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'date_joined',
            'first_name',
            'last_name',
        ]
