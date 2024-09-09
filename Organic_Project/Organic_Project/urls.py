"""Organic_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,re_path,include
# from django.urls import re_path

# for media store purpose
from django.conf import settings

#api and documendaction 
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Organic Store API",
      default_version='v1',
      description="Organic Store",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="basilahamed.h@changepond.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
     path('admin/', admin.site.urls),
#    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path("api/Category/",include('category_Table.urls')),
     path("api/Product_Table/",include("Product_Table.urls")),
    #  path("api/Checkout_Table/",include("Checkout_Table.urls")),
     path("api/users/",include("User_Table.urls")),
# <<<<<<< HEAD
     path("api/coupon/",include("Coupon_Table.urls")),
     path("api/shipping/",include("Shipping_Table.urls")),
# =======
     path("api/cart/",include("cart_table.urls")),
     path("api/orders/",include("Order_Table.urls")),
     path("api/feedback/",include("Feedback_table.urls")),
# >>>>>>> 51fd64acc2d5c0431dfe1874877c6c3dffd0ddd7
    #  path("api/User/",include("User.urls")),
    path("api/admin/",include("admin_table.urls")),
     path('api/token/',swagger_auto_schema(method='post',security=[])(TokenObtainPairView.as_view()),name='token_obtain_pair'),
    path('api/token/refresh/',swagger_auto_schema(method='post',security=[])(TokenRefreshView.as_view()),name='token_refresh'),
 
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)