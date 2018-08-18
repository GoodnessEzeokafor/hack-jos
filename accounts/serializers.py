from rest_framework import serializers
from . import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Participator
        fields = (
        		'full_name', 
        		'username', 
        		'email', 
        		'team', 
        		'startup',
        		'startup_overview',
        	 	)
        
        