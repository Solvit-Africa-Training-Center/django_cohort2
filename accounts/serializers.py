from rest_framework import serializers
from django.db import transaction
from .models import User, Role


# ==================================================
# BASE REGISTER SERIALIZER
# ==================================================


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
            # address fields
            "country",
            "province",
            "district",
            "sector",
            "cell",
            "village",
            "street",
            "description",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs


# BUYER RegisterSerializer

from .models import Address

class BuyerRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop("re_password")

        # Extract address fields
        address_data = {
            key: validated_data.pop(key, "")
            for key in [
                "country", "province", "district", "sector", "cell",
                "village", "street", "description"
            ]
        }

        buyer_role, _ = Role.objects.get_or_create(name=Role.BUYER)

        # Create user
        user = User.objects.create_user(
            role=buyer_role,
            **validated_data
        )

        # Create address if at least one field is filled
        if any(address_data.values()):
            Address.objects.create(user=user, **address_data)

        return user

    
# SELLER RegisterSerializer


class SellerRegisterSerializer(RegisterSerializer):
    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop("re_password")

        # Extract address fields
        address_data = {
            key: validated_data.pop(key, "")
            for key in [
                "country", "province", "district", "sector", "cell",
                "village", "street", "description"
            ]
        }

        seller_role, _ = Role.objects.get_or_create(name=Role.SELLER)

        # Create user
        user = User.objects.create_user(
            role=seller_role,
            **validated_data
        )

        # Create address if any fields provided
        if any(address_data.values()):
            Address.objects.create(user=user, **address_data)

        return user

