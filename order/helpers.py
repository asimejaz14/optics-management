import hashlib
import time
from base64 import encode

from common import enums
from common.enums import OrderStatus
from common.utils import send_message


def generate_tracking_number():
    return (hashlib.md5((str(time.time()) + "!salt!").encode()).hexdigest()[:8]).upper()


def check_order_status_update(request, order):
    # check if order status is updated
    if request.data.get('order_status'):
        if request.data.get('order_status') == OrderStatus.INPROGRESS:
            text_msg = enums.IN_PROGRESS_TEXT.replace("$CUSTOMER", order.customer_name)
            text_msg = text_msg.replace("$TRACKING_NUMBER", order.tracking_number)
            send_message(order.customer_contact, text_msg)
        elif request.data.get('order_status') == OrderStatus.READY:
            text_msg = enums.READY_TEXT.replace("$CUSTOMER", order.customer_name)
            text_msg = text_msg.replace("$TRACKING_NUMBER", order.tracking_number)
            send_message(order.customer_contact, text_msg)
        elif request.data.get('order_status') == OrderStatus.COMPLETED:
            text_msg = enums.COMPLETED_TEXT.replace("$CUSTOMER", order.customer_name)
            send_message(order.customer_contact, text_msg)
