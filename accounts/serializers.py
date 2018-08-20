from rest_framework import serializers
from .models import (
	User,
	Team,
	Participant
)
from .forms import (
	UserCreationForm
)

class ParticipantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participant
		fields = (
			'id',
			'full_name',
			'email',
		)


class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = (
				'id',
				'team_name',
				'team_lead',
				'team_members',
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