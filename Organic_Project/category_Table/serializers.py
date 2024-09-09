from rest_framework import serializers
from .models import Category_Table

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Table
        fields = ['id',"Category_Name"]
        read_only_fields=['id']