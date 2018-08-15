from rest_framework import serializers
from . import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ('full_name', 'username', 'email', 'team', 'startup', 'is_active', 'admin', 'staff')
        
        