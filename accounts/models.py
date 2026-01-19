import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator


# ==================================================
# ROLE MODEL
# ==================================================
class Role(models.Model):
    """
    Defines system roles such as ADMIN, BUYER, SELLER.
    """

    ADMIN = "ADMIN"
    BUYER = "BUYER"
    SELLER = "SELLER"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (BUYER, "Buyer"),
        (SELLER, "Seller"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        unique=True
    )

    description = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==================================================
# USER MANAGER
# ==================================================
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        if not full_name:
            raise ValueError("Full name is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        role, _ = Role.objects.get_or_create(name=Role.ADMIN)

        extra_fields.setdefault("role", role)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        return self.create_user(
            email=email,
            full_name=full_name,
            password=password,
            **extra_fields
        )


# ==================================================
# USER MODEL
# ==================================================
class User(AbstractBaseUser, PermissionsMixin):
    """
    Represents any system user:
    - Individual
    - Company
    - Shop
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(_("email address"), unique=True)

    full_name = models.CharField(
        _("full name / company / shop name"),
        max_length=255
    )

    phone_number = models.CharField(
        _("phone number"),
        max_length=13,
        unique=True,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(13)
        ]
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="users"
    )

    # Auth & status fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)

    # Optional business fields
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.full_name

    # --------------------------------------------------
    # PRODUCT RELATION (FOR OTHER GROUP – FUTURE USE)
    # --------------------------------------------------
    """
    Products model can safely link like this later:

    class Product(models.Model):
        seller = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="products",
            limit_choices_to={"role__name": "SELLER"}
        )
    """


# ==================================================
# ADDRESS MODEL
# ==================================================
class Address(models.Model):
    """
    Stores delivery / billing addresses for users.
    A user can have multiple addresses.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    street = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    is_default = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.district}, {self.province}"
