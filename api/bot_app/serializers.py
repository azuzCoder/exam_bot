from rest_framework import serializers

from .models import BotUser


class BotUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotUser
        fields = ['id', 'from_id', 'full_name', 'phone_number', 'address', 'passport_number', 'passport_image']
