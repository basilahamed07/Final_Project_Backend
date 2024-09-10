# views.py (in your Django app)

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer
from User_Table.models import CustomUser  # Import the CustomUser model

class SendEmailView(APIView):
    """
    API View to send an email to a user based on their user ID.
    """

    def get(self, request, user_id):
        # Get the user from the database using the provided user_id
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Prepare the data for the serializer
        data = {
            'recipient_email': user.email,  # Get the user's email
            'subject': request.GET.get('subject', 'Test Email from Django'),  # Get subject from query params or default
            'message': request.GET.get('message', 'This is a test email sent via Django REST Framework.')  # Get message or default
        }

        # Validate the data using the serializer
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            # Extract the validated data
            recipient_email = serializer.validated_data['recipient_email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            
            # Send the email
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,  # Sender's email (configured in settings.py)
                    [recipient_email],  # Recipient's email
                    fail_silently=False,
                )
                return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
