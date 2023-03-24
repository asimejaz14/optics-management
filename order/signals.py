from django.db.models.signals import post_save
from django.dispatch import receiver

from common.utils import send_message
from order.models import Order


@receiver(post_save, sender=Order)
def send_notification(sender, instance, created, **kwargs):
    if created:
        send_message(instance.customer_contact, f"Order created with tracking no. {instance.tracking_number}")
