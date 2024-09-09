from rest_framework import serializers
from .models import Shipping_Table

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Table
        fields = ['id',"Shipping_id","shipping_status","tracking_id"]
        read_only_fields=['id',"Shipping_id","tracking_id"]