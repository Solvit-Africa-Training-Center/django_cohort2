

from rest_framework import viewsets, mixins
from drf_yasg.utils import swagger_auto_schema
from .models import Category, SubCategory, Product, ProductImage
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, ProductImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Add a new category.",
        request_body=CategorySerializer,
        responses={201: CategorySerializer},
        examples={
            'application/json': {
                'name': 'Electronics',
                'image_url': 'https://example.com/electronics.jpg',
                'is_active': True
            }
        }
    )
    def create(self, request, *args, **kwargs):
        """
        Docstring for create
        
        :param self: Description
        :param request: Description
        :param args: Description
        :param kwargs: Description
        """        
        return super().create(request, *args, **kwargs)

class SubCategoryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    @swagger_auto_schema(
        operation_description="Add a new subcategory.",
        request_body=SubCategorySerializer,
        responses={201: SubCategorySerializer},
        examples={
            'application/json': {
                'category': 'category-uuid',
                'name': 'Mobile Phones',
                'is_active': True
            }
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ProductViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="Add a new product with images.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer},
        examples={
            'application/json': {
                'sub_category_id': 'subcategory-uuid',
                'name': 'iPhone 15',
                'description': 'Latest Apple iPhone',
                'price': '999.99',
                'discount_price': '899.99',
                'is_available_inStock': True,
                'publish': True,
                'rating': 5.0,
                'images': [
                    {'image_url': 'https://example.com/image1.jpg'},
                    {'image_url': 'https://example.com/image2.jpg'}
                ]
            }
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an existing product.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update an existing product.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    @swagger_auto_schema(
        operation_description="Add a new product image to an existing product. Use multipart/form-data: set 'product' as the product UUID and 'image_url' as the file.",
        manual_parameters=[],
        responses={201: ProductImageSerializer},
        consumes=["multipart/form-data"],
        examples={
            'multipart/form-data': {
                'product': 'product-uuid',
                'image_url': '(select a file)'
            }
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
