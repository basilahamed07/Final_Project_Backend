# serializers.py (in your Django app)

from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    recipient_email = serializers.EmailField()  # Field for recipient email
    subject = serializers.CharField(max_length=255, default='No Subject')  # Optional subject
    message = serializers.CharField(default='No Message')  # Optional message
