from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list):
    """
    Utility function to send an email using Django's send_mail function.
    """
    # Send email
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender email
            recipient_list,  # List of recipient emails
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
