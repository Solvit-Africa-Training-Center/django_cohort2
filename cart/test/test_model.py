
from django.test import TestCase
from cart.models import Cart, CartItem
from accounts.models import User, Role
from products.models import Product, Category, SubCategory

import datetime

class CartTestCase(TestCase):
    def setUp(self):
      
        self.role, _ = Role.objects.get_or_create(name=Role.BUYER)
        
        self.user = User.objects.create(
            email="test@test.com",
            full_name="Test User",
            role=self.role
        )
        
        self.cart = Cart.objects.create(
            user=self.user,
            session_id="12",
            status="active"
        )
        
    def test_cart_creation(self):
        self.assertEqual(self.cart.status, 'active')
        self.assertIsNotNone(self.cart.created_at)


class CartItemTestCase(TestCase):
    def setUp(self):
      
        self.role, _ = Role.objects.get_or_create(name=Role.BUYER)
        self.user = User.objects.create(
            email="test2@test.com",
            full_name="Test User 2",
            role=self.role
        )
        self.cart = Cart.objects.create(
            user=self.user,
            session_id="13",
            status="active"
        )
       
        self.category = Category.objects.create(name="Test Category")
        self.subcategory = SubCategory.objects.create(name="Test Subcategory", category=self.category)
      
        self.product = Product.objects.create(
            name="Test Product",
            sub_category=self.subcategory,
            price=10.00
        )
        
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=25
        )
    
    def test_cartitem_creation(self):
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 25)
        self.assertIsNotNone(self.cart_item.created_at)
            
       
    