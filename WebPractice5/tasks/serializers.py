from rest_framework import serializers
from models import User, Tasks, Categories

class UserSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    