from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Role


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "phone_number",
            "role",
            "password",
        ]

    def create(self, validated_data):
        # Extract role explicitly
        role = validated_data.pop("role")

        user = User.objects.create_user(
            role=role,
            **validated_data
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data["user"] = user
        return data


class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "phone_number",
        ]


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "phone_number",
        ]
