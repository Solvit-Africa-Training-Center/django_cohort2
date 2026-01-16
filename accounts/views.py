from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BuyerRegisterSerializer, SellerRegisterSerializer

class AuthViewSet(viewsets.ViewSet):
    """
    Auth-related endpoints: buyer/seller registration.
    """

    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"], url_path="register/buyer")
    def register_buyer(self, request):
        serializer = BuyerRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Buyer registered successfully"},
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=["post"], url_path="register/seller")
    def register_seller(self, request):
        serializer = SellerRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Seller registered successfully"},
            status=status.HTTP_201_CREATED
        )
