class Status:
    DELETED = 0
    ACTIVE = 1
    INACTIVE = 2
    BLOCKED = 3


class OrderStatus:
    PLACED = 0
    INPROGRESS = 1
    READY = 2
    COMPLETED = 3


USER_TYPE = [
    (1, 'SUPER_ADMIN'),
    (2, 'ADMIN')
]

STATUS = [
    (0, 'DELETED'),
    (1, 'ACTIVE'),
    (2, 'INACTIVE'),
    (3, 'BLOCKED'),
]

ORDER_STATUS = [
    (0, 'PLACED'),
    (1, 'INPROGRESS'),
    (2, 'READY'),
    (3, 'COMPLETED'),
]


# Mobile text msgs
PLACED_TEXT = "Dear $CUSTOMER, your order has been created with tracking no. $TRACKING_NUMBER."
IN_PROGRESS_TEXT = "Dear $CUSTOMER, your order with tracking no. $TRACKING_NUMBER is now in-progress!"
READY_TEXT = "Dear $CUSTOMER, your order with tracking no. $TRACKING_NUMBER is ready to pick up."
COMPLETED_TEXT = "Dear $CUSTOMER, thank you for shopping with us."


ORDER_SORTING_KEYS = {
    "created_at": "created_at",
    "customer_name": "name",
    "tracking_number": "tracking_number",
    "updated_at": "updated_at",
    "status": "order_status",
}
