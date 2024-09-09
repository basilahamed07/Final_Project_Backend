from django.shortcuts import render
from.models import Product_Table
from .serializers import Product_Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status,parsers
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication 

# Create your views here.
class Product_ViewSet(ModelViewSet):
    queryset = Product_Table.objects.all()
    serializer_class = Product_Serializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser,parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

















    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return Product_Serializer
    #     elif self.action=='create':
    #         return Product_Serializer
    #     return self.serializer_class
    # @action(methods=['POST'],detail=True,url_path='upload-image')
    # def upload_image(self,request,pk=None):
    #     Catagory_Obj =self.get_object()
    #     serializer=self.get_serializer(Catagory_Obj,data=request.data)
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
    #                 'message': 'dish Image uploaded Successfully'
    #             })
 
# #get all Product_Table
#     def list(self,request):
#         try:
#             Catagory_Obj = Product_Table.objects.all()
#             serializer = self.get_serializer(Catagory_Obj,many=True)
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
        
        
# # create an dish 
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
#                 'status': status.HTTP_201_CREATED,
#                 'data': serializer.data,
#                 'message': 'Dish created successfully'
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
        
# # get single dish

#     def retrive(self,request,pk=None):
#         try:
#             id = pk
#             if id is not None:
#                 Catagory_Obj = self.get_object()
#                 serializer = self.get_serializer(Catagory_Obj)
#                 return Response({
#                    'status': status.HTTP_200_OK,
#                    'data':serializer.data
#                 })
            

 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
# #update all fields of dish
#     def update(self,request,pk=None):
#         try:
#             Catagory_Obj = self.get_object()
#             serializer = self.get_serializer(Catagory_Obj,data=request.data,partial=False)
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
#                     'message': 'Product_Table Updated Successfully'
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
#     #update specifie
#     def partial_update(self,request,pk=None):
#         try:
#             Catagory_Obj = self.get_object()
#             serializer = self.get_serializer(Catagory_Obj,data=request.data,partial=True)
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
#                     'message': 'Dish Partial Updated Successfully'
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
 
#     def destroy(self,request,pk):
#         try:
#             id=pk
#             Catagory_Obj = self.get_object()
#             Catagory_Obj.delete()
 
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'message':'Dish deleted successfully'
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
        