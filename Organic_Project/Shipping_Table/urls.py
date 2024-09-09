from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipingViewSet
 
router = DefaultRouter()
router.register('', ShipingViewSet, basename='Shipping')
app_name ='Shipping'
 
urlpatterns=[
    path('', include(router.urls))
]