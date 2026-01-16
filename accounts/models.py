import uuid
import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator



class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault("user_type", User.ADMIN)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        return self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )



class User(AbstractUser, PermissionsMixin):

    ADMIN = "ADMIN"
    BUYER = "BUYER"
    SELLER = "SELLER"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (BUYER, "Buyer"),
        (SELLER, "Seller"),
    ]

    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user_type = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=BUYER
    )

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)

    phone_number = models.CharField(
        _("phone number"),
        max_length=13,
        unique=True,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(13)
        ]
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class SellerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="seller_profile"
    )

    shop_name = models.CharField(max_length=255)
    shop_description = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name


