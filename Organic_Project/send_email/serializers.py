# serializers.py
from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    recipient_email = serializers.EmailField()
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField()
