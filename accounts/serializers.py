from rest_framework import serializers
from .models import User, SellerProfile
from django.db import transaction


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "re_password",
            "user_type",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs


# Buyer registration
class BuyerRegisterSerializer(RegisterSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if not attrs.get("first_name") or not attrs.get("last_name"):
            raise serializers.ValidationError(
                "Buyers must provide first name and last name"
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("re_password")

        user = User.objects.create_user(
            user_type=User.BUYER,
            **validated_data
        )
        return user
# Seller registration
class SellerRegisterSerializer(RegisterSerializer):
    shop_name = serializers.CharField(required=True)
    shop_description = serializers.CharField(required=False, allow_blank=True)

    class Meta(RegisterSerializer.Meta):
        fields = RegisterSerializer.Meta.fields + (
            "shop_name",
            "shop_description",
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if not attrs.get("shop_name"):
            raise serializers.ValidationError(
                "Sellers must provide a shop name"
            )

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        shop_name = validated_data.pop("shop_name")
        shop_description = validated_data.pop("shop_description", "")
        validated_data.pop("re_password")

        user = User.objects.create_user(
            user_type=User.SELLER,
            **validated_data
        )

        SellerProfile.objects.create(
            user=user,
            shop_name=shop_name,
            shop_description=shop_description,
        )

        return user


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         User.objects.filter(id=user.id).update(
#             last_login=datetime.datetime.now())
#         user.save()
#         token = super().get_token(user)
#         # Add custom claims
#         token["first_name"] = user.first_name
#         token["last_name"] = user.last_name
#         token["phone_number"] = user.phone_number
#         token["email"] = user.email
#         token["user_type"] = user.user_type
  