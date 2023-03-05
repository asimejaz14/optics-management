import uuid

from django.db import models

from common.enums import STATUS, Status
from common.models import DateTimeLog
from common.validators import validate_image


# Create your models here.
class Customer(DateTimeLog):

    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)
    subscription_is_valid = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(
        max_length=300, upload_to="user_profile_images", null=True, validators=[validate_image]
    )
