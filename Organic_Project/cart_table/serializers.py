from .models import  cart_table
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class carttable_Serializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only = True)
    class Meta:
        model = cart_table
        fields = ["id","user_id","product_ids","quandity","total_price"]
        read_only_fields=['id']