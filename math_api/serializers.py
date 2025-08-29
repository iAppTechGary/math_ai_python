from rest_framework import serializers
from .models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "udid","token", "device_model", "device_name", "app_version", "os_version","ip"
          
        ]
