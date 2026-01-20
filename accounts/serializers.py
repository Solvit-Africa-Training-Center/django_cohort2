from rest_framework import serializers
from .models import User, Role, Address


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    re_password = serializers.CharField(write_only=True)

    # Optional address fields
    country = serializers.CharField(required=False, allow_blank=True)
    province = serializers.CharField(required=False, allow_blank=True)
    district = serializers.CharField(required=False, allow_blank=True)
    sector = serializers.CharField(required=False, allow_blank=True)
    cell = serializers.CharField(required=False, allow_blank=True)
    village = serializers.CharField(required=False, allow_blank=True)
    street = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            "email",
            "full_name",
            "phone_number",
            "password",
            "re_password",
            "country",
            "province",
            "district",
            "sector",
            "cell",
            "village",
            "street",
            "description",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "re_password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs


# BUYER

class BuyerRegisterSerializer(RegisterSerializer):

    def create(self, validated_data):
        validated_data.pop("re_password")

        # Extract address fields
        address_fields = [
            "country", "province", "district", "sector",
            "cell", "village", "street", "description"
        ]

        address_data = {}
        for field in address_fields:
            address_data[field] = validated_data.pop(field, "")

        buyer_role, _ = Role.objects.get_or_create(name=Role.BUYER)

        # Create buyer user
        user = User.objects.create_user(
            role=buyer_role,
            **validated_data
        )

        # Create address only if at least one value exists
        if any(address_data.values()):
            Address.objects.create(user=user, **address_data)

        return user


# SELLER:



class SellerRegisterSerializer(RegisterSerializer):

    def create(self, validated_data):
        validated_data.pop("re_password")

        address_fields = [
            "country", "province", "district", "sector",
            "cell", "village", "street", "description"
        ]

        address_data = {}
        for field in address_fields:
            address_data[field] = validated_data.pop(field, "")

        seller_role, _ = Role.objects.get_or_create(name=Role.SELLER)

        # Create seller user
        user = User.objects.create_user(
            role=seller_role,
            **validated_data
        )

        if any(address_data.values()):
            Address.objects.create(user=user, **address_data)

        return user
    
