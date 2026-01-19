from rest_framework import serializers
from .models import Category, SubCategory, Product, ProductImage, Feedback

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url', 'is_active', 'created_at', 'updated_at']

class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'category_name', 'name', 'is_active', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    sub_category_name = serializers.ReadOnlyField(source='sub_category.name')
    category_name = serializers.ReadOnlyField(source='sub_category.category.name')

    class Meta:
        model = Product
        fields = [
            'id', 'sub_category', 'sub_category_name', 'category_name', 'name', 
            'description', 'price', 'discount_price', 'is_available_inStock', 
            'is_active', 'rating', 'created_at', 'updated_at'
        ]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'file', 'created_at', 'updated_at']

class FeedbackSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Feedback
        fields = ['id', 'product', 'user', 'user_username', 'rating', 'message', 'created_at']
