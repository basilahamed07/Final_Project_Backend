from django.shortcuts import render
from.models import cart_table
from .serializers import carttable_Serializer
from rest_framework.viewsets import ModelViewSet
# from rest_framework.exceptions import APIException
# from rest_framework.response import Response
from rest_framework import status,parsers
# from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication 

# Create your views here.
class cartVieset(ModelViewSet):

    queryset = cart_table.objects.all()    # table name
    serializer_class = carttable_Serializer  # serializer name
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser) # for photo upload
    authentication_classes = [JWTAuthentication] # auth purpose
    permission_classes = [permissions.IsAuthenticated]
    

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return carttable_Serializer
    #     elif self.action=='create':
    #         return carttable_Serializer
    #     return self.serializer_class