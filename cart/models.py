
from django.db import models
from products.models import Product
from accounts.models import User
import uuid
import datetime

class Cart(models.Model):
    STATUS_CHOICES=[
        ('active','Active'),
        ('completed','Completed')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    session_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [ 'cart','product']

    def __str__(self):
        return f"{self.quantity} x {self.product.name} " 


