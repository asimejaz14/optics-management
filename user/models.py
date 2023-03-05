import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from common.enums import STATUS, Status, USER_TYPE
from common.models import DateTimeLog
from common.validators import validate_image
# from customer.models import Customer


# Create your models here.
class User(AbstractUser, DateTimeLog):
    """User model extending Django's default user model"""

    # User identifier
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    # Username, optional
    username = None
    # Email, used as USERNAME field by User model
    email = models.CharField(max_length=200, unique=True, null=False, blank=False)
    # User type FK
    user_type = models.CharField(max_length=1, choices=USER_TYPE, default=1)

    # reset_token = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)

    # User image
    image = models.ImageField(
        max_length=300, upload_to="user_profile_images", null=True, validators=[validate_image]
    )

    # designation = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=200, unique=True, null=True, blank=True)
    # Read, Write and Delete permissions

    # User customer
    # customer = models.ForeignKey(
    #     Customer, null=True, blank=True, on_delete=models.CASCADE
    # )

    gender = models.CharField(max_length=100, null=True, blank=True)
    is_active = True
    is_verified = models.BooleanField(null=True, default=False)
    is_staff = None
    is_superuser = None
    # Use EMAIL insted of USERNAME
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
            super(User, self).save(*args, **kwargs)
