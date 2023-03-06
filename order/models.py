from django.db import models

from common.enums import ORDER_STATUS, OrderStatus, STATUS, Status
from common.models import DateTimeLog
from order.helpers import generate_tracking_number
from django.utils import timezone


# Create your models here.
class Order(DateTimeLog):
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    customer_contact = models.CharField(max_length=200, null=True, blank=True)
    customer_dob = models.DateField(null=True, blank=True)
    booking_datetime = models.DateTimeField(default=timezone.now)
    delivery_datetime = models.DateTimeField(null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
    advance_payment = models.IntegerField(null=True, blank=True)
    remaining_balance = models.IntegerField(null=True, blank=True)
    frame = models.CharField(max_length=200, null=True, blank=True)
    lens = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)
    r_sph = models.CharField(max_length=20, null=True, blank=True)
    r_cyl = models.CharField(max_length=20, null=True, blank=True)
    r_axis = models.CharField(max_length=20, null=True, blank=True)
    l_sph = models.CharField(max_length=20, null=True, blank=True)
    l_cyl = models.CharField(max_length=20, null=True, blank=True)
    l_axis = models.CharField(max_length=20, null=True, blank=True)
    delivered_by = models.CharField(max_length=200, null=True, blank=True)
    checked_by = models.CharField(max_length=200, null=True, blank=True)
    delivered_datetime = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS, default=OrderStatus.PLACED)
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)
    tracking_number = models.CharField(max_length=50, null=True, blank=True, default=generate_tracking_number)

    def __str__(self):
        return self.tracking_number

    def save(self, *args, **kwargs):
        if self.total_cost and self.advance_payment:
            self.remaining_balance = self.total_cost - self.advance_payment
        super(Order, self).save(*args, **kwargs)
