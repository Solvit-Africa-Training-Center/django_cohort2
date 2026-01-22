

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-images', ProductImageViewSet, basename='productimage')

urlpatterns = [
    path('', include(router.urls)),
]
