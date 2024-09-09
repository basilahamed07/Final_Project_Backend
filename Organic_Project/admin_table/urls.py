# urls.py

from django.urls import path
from .views import UserListView,UserDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user_list'),
     path('admin/users/<int:user_id>/delete/', UserDeleteView.as_view(), name='user_delete'),
]