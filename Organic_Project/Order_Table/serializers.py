from rest_framework import serializers
from .models import Order_table
from User_Table.models import CustomUser
from Shipping_Table.models import Shipping_Table

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_table
        fields = ['id', 'user_id', 'shipping', 'order_date', 'total_price', 'product_ids', 'quantity']
        read_only_fields = ['id', 'order_date']
