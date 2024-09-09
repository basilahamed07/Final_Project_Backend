from rest_framework import serializers
from .models import Order_table
from User_Table.models import CustomUser
from Shipping_Table.models import Shipping_Table

class OrderSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user_id', write_only=True)
    shipping = serializers.PrimaryKeyRelatedField(queryset=Shipping_Table.objects.all(), required=False)

    class Meta:
        model = Order_table
        fields = ['id', 'user', 'shipping', 'order_date', 'total_price', 'product_ids', 'quantity']
        read_only_fields = ['id', 'order_date']
