from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Product_ViewSet
 
router = DefaultRouter()
router.register('', Product_ViewSet, basename='Product')
app_name ='Product'
 
urlpatterns=[
    path('', include(router.urls))
]