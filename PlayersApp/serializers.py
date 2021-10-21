from rest_framework import serializers
from PlayersApp.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields=('PlayerId', 'FirstName', 'LastName', 'CurrentClub', 'nationallity', 'DateOfBirth', 'Position', 'LastModified')