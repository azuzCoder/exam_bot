from rest_framework import serializers

from .models import BotUser, BotAdmin


class BotUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotUser
        fields = ['id', 'from_id', 'full_name', 'phone_number', 'address',
                  'passport_number', 'passport_image', 'solution']


class BotAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotAdmin
        fields = ['id', 'from_id']
