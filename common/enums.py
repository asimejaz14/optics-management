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
