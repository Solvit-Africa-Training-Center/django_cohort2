from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, SubCategoryViewSet, ProductViewSet, 
    ProductImageViewSet, FeedbackViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
          path('', include(router.urls)),
]
