from django.urls import path
 
from .views import ManageUserView, RegisterUserAPIView
 
app_name = 'User'
 
urlpatterns = [
    path('register',RegisterUserAPIView.as_view()),
    path('get_user',ManageUserView.as_view(),name="get_user")
]