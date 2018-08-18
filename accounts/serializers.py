from rest_framework import serializers
from .models import (
	User,
	Participator
)
from .forms import (
	UserCreationForm
)


# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#     	model = User
#     	fields = (
#     			'username',
#     			'email',
#     			'password'
#     	)

# class ParticipatorSerializer(serializers.ModelSerializer):
# 	pass
# 	