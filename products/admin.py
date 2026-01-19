from django.contrib import admin
from .models import Category, SubCategory, Product, ProductImage, Feedback


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',    'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category', 'name', 'price', 'discount_price', 'is_available_inStock', 'is_active', 'created_at')
    list_filter = ('sub_category', 'is_active', 'is_available_inStock')
    search_fields = ('name',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at')
    search_fields = ('product__name',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'user__username')
