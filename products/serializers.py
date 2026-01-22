from rest_framework import serializers
from .models import Category, SubCategory, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    # name = serializers.CharField(max_length=100)
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return value



class SubCategorySerializer(serializers.ModelSerializer):
    #category = CategorySerializer(read_only=True)
    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ProductImage
        fields ="__all__"

  


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    sub_category = SubCategorySerializer(read_only=True)
    sub_category_id = serializers.UUIDField(write_only=True)
   
    class Meta:
        model = Product
        fields = ['id', 'sub_category', 'sub_category_id', 'name', 'description', 'price', 'discount_price',
                  'is_available_inStock', 'publish', 'rating', 'created_at', 'updated_at', 'images']


    def create(self, validated_data):
        images_data = self.context['request'].data.pop('images', [])
        name = self.context['request'].data.pop('name', [])
        if Product.objects.filter(name=name).exists():
            raise serializers.ValidationError("Product with this name already exists.")

        product = Product.objects.create(**validated_data)

        if images_data:
            for image_data in images_data:
                ProductImage.objects.create(product=product, image_url=image_data)
        
        sub_category_id = self.context['request'].data.get('sub_category_id', None)
        if sub_category_id:
            sub_category, created = SubCategory.objects.get_or_create(id=sub_category_id)
            product.sub_category = sub_category
            product.save()
        return product
    
    
