from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import feedbackViewSet
 
router = DefaultRouter()
router.register('', feedbackViewSet, basename='Feedback')
app_name ='Feedback'
 
urlpatterns=[
    path('', include(router.urls))
]