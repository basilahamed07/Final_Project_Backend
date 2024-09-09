from rest_framework import serializers
from .models import Coupon_Table

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon_Table
        fields = ['id',"discount","code"]
        read_only_fields=['id',"code"]