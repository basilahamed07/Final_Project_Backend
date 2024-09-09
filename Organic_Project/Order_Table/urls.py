from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewset
 
router = DefaultRouter()
router.register('', OrderViewset, basename='orders')
app_name ='orders'
 
urlpatterns=[
    path('', include(router.urls))
]