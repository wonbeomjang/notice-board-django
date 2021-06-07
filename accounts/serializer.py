from rest_framework import serializers

from django.contrib.auth import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email')