from django.db.models.signals import post_save
from django.dispatch import receiver

from common.enums import PLACED_TEXT
from common.utils import send_message
from order.models import Order


@receiver(post_save, sender=Order)
def send_notification(sender, instance, created, **kwargs):
    if created:
        ...
        # text_msg = PLACED_TEXT.replace("$CUSTOMER", instance.customer_name)
        # text_msg = text_msg.replace("$TRACKING_NUMBER", instance.tracking_number)
        # send_message(instance.customer_contact, text_msg)
