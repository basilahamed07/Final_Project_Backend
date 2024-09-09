from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Feedback

from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from .serializers import feedbackSerializer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication




# Create your views here.

class feedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = feedbackSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
 
