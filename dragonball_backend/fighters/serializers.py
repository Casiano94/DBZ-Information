from rest_framework import serializers
from .models import Fighter

class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ['name', 'description', 'image']
