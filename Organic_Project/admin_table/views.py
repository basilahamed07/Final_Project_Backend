# views.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from User_Table.models import CustomUser
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status

class UserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        
        users = CustomUser.objects.all()
        user_data = [{'id': user.id, 'username': user.username, 
                      "phone_number": user.phone_number, 
                      "address": user.first_line, 
                      "city":user.city, 
                      "pincode":user.pincode, 
                      "card_id":user.cart_product_ids} for user in users]

        return Response(user_data)
    
class UserDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)  
   