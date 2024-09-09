from django.shortcuts import render
from .models import Coupon_Table
# from .serializers import CatogorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from .serializers import CouponSerializer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

class CouponViewSet(ModelViewSet):
    queryset = Coupon_Table.objects.all()
    serializer_class = CouponSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
 


"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NjQ2MDg5LCJpYXQiOjE3MjU1NTk2ODksImp0aSI6ImU2YzUwMmEyYzg0MTQxZjA4NjdhNjQ5MGE3N2ZjOWQ4IiwidXNlcl9pZCI6MX0.y8C22tIPDkX2SUVs_yvaXnMA6XjD302Rs8eBJg3Jx4s"














    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CouponSerializer
    #     elif self.action == 'create':
    #         return CouponSerializer
    #     # elif self.action == 'upload_image':
    #     #     return catogoryImageSerializar
    #     return self.serializer_class



#------------------------------->>>>getting image<<<<<-------------------------------
#image upload

    # @action(methods=['POST'],detail=True,url_path='upload-image')
    # def upload_image(self,request,pk=None):
    #     catogory_objs =self.get_object()
    #     serializer=self.get_serializer(catogory_objs,data=request.data)
    #     if not serializer.is_valid():
    #         return Response({
    #                 'status': status.HTTP_400_BAD_REQUEST,
    #                 'data':serializer.errors,
    #                 'message':'Inavlid Data'
    #             })
    #     serializer.save()
    #     return Response({
    #                 'status': status.HTTP_200_OK,
    #                 'data':serializer.data,
    #                 'message': 'catogory Image Successfully'
    #             })





#------------------------------->>>>getting catogory<<<<<-------------------------------

# #get all catogorys
#     def list(self,request):
#         try:
#             catogory_objs = Coupon_Table.objects.all()
#             serializer = self.get_serializer(catogory_objs,many=True)
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'data':serializer.data
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
 

# #------------------------------->>>>adding catogory<<<<<-------------------------------

# #add an catogory
#     def create(self,request):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             if not serializer.is_valid():
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'data':serializer.errors,
#                     'message':'Inavlid Data'
#                 })
#             serializer.save()
#             return Response({
#                     'status': status.HTTP_200_OK,
#                     'data':serializer.data,
#                     'message': 'catogory Added Successfully'
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
 
# #------------------------------->>>>getting single data<<<<<-------------------------------
# #get single catogory
 
#     def retrieve(self,request,pk=None):
#         try:
#             id = pk
#             if id is not None:
#                 catogory_objs = self.get_object()
#                 serializer = self.get_serializer(catogory_objs)
#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'data':serializer.data
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
 
# #------------------------------->>>>update data all<<<<<-------------------------------
#     def update(self,request,pk=None):
#         try:
#             catogory_objs = self.get_object()
#             serializer = self.get_serializer(catogory_objs,data=request.data,partial=False)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'data':serializer.errors,
#                     'message':'Inavlid Data'
#                 })
#             serializer.save()
#             return Response({
#                     'status': status.HTTP_200_OK,
#                     'data':serializer.data,
#                     'message': 'catogory Updated Successfully'
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
 
#  #------------------------------->>>>update specific data<<<<<-------------------------------
# #update specifie
#     def partial_update(self,request,pk=None):
#         try:
#             catogory_objs = self.get_object()
#             serializer = self.get_serializer(catogory_objs,data=request.data,partial=True)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'data':serializer.errors,
#                     'message':'Inavlid Data'
#                 })
#             serializer.save()
#             return Response({
#                     'status': status.HTTP_200_OK,
#                     'data':serializer.data,
#                     'message': 'catogory Partial Updated Successfully'
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
 
#  #------------------------------->>>>Delete specific data<<<<<-------------------------------
#     def destroy(self,request,pk):
#         try:
#             id=pk
#             catogory_objs = self.get_object()
#             catogory_objs.delete()
 
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'message':'catogory deleted successfully'
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })