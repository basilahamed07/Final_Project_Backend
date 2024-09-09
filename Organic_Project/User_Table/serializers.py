from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser  

class UserSerializer(serializers.ModelSerializer):
    """UserSerializer to get user details using JWT authentication."""

    cart_product_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )
    quantities = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "phone_number", "first_line", "city", "state", "pincode", "cart_product_ids", "quantities"]

class RegisterSerializer(serializers.ModelSerializer):
    """RegisterSerializer to create user."""

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password = serializers.CharField(
        required=True, 
        validators=[validate_password],
        write_only=True
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    first_line = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    pincode = serializers.CharField(required=False)

    cart_product_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        default=list  # Default to an empty list
    )
    quantities = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        default=list  # Default to an empty list
    )
    
    class Meta:
        model = CustomUser
        fields = ["email", "password", "confirm_password", "first_name", "last_name", "phone_number", "first_line", "city", "state", "pincode", "cart_product_ids", "quantities"]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
 
    def create(self, validated_data):
        validated_data.pop('confirm_password')  

        cart_product_ids = validated_data.pop('cart_product_ids', [])
        quantities = validated_data.pop('quantities', [])

        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            first_line=validated_data['first_line'],
            city=validated_data['city'],
            state=validated_data['state'],
            pincode=validated_data['pincode'],
            cart_product_ids=cart_product_ids,
            quantities=quantities
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
