from rest_framework import serializers

class TempUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    knows = serializers.CharField(max_length=20)
    learning = serializers.CharField(max_length=20)
    