from rest_framework import serializers
from .models import Product_Table
# from category_Table.serializers import CategorySerializer

class Product_Serializer(serializers.ModelSerializer):
    P_Category_id = serializers.IntegerField()

    class Meta:
        model = Product_Table   
        fields = ["id","P_Name","P_description","P_Price","P_Stock","P_Category_id","P_Brand","P_image"]
        read_only_fields=['id']