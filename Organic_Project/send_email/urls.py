# urls.py (in your Django app)

from django.urls import path
from .views import SendEmailView  # Import the view

urlpatterns = [
    path('send-email/<int:user_id>/', SendEmailView.as_view(), name='send_email'),
]
