from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED

from common import enums
from common.enums import Status, OrderStatus, ORDER_SORTING_KEYS
from common.utils import send_message
from order.helpers import check_order_status_update
from order.models import Order
from order.serializers import OrderSerializer


class OrderController:

    @classmethod
    def get_order(cls, request, tracking_number=None):
        try:
            # single order detail
            if tracking_number:
                order = Order.objects.filter(tracking_number__iexact=tracking_number, status=Status.ACTIVE).first()
                if not order:
                    return Response(data=None, status=HTTP_204_NO_CONTENT)
                serialized_order = OrderSerializer(order)
                return Response(data=serialized_order.data, status=HTTP_200_OK)

            # all orders detail
            kwargs = {}
            q = request.query_params.get("q")
            date = request.query_params.get("date")
            order_by = request.query_params.get("order_by", "created_at")
            order = request.query_params.get("order", "desc")
            limit = request.query_params.get("limit")
            offset = request.query_params.get("offset")
            # export = request.query_params.get("export")

            if date:
                kwargs['created_at__date'] = date
            if order == "asc":
                sort = ORDER_SORTING_KEYS[order_by]
            else:
                sort = "-" + ORDER_SORTING_KEYS[order_by]

            kwargs['status'] = Status.ACTIVE

            orders = Order.objects.filter(**kwargs).order_by(sort)
            if q:
                orders = orders.filter(Q(customer_name__icontains=q) | Q(tracking_number=q))
            count = orders.count()
            if limit and offset:
                pagination = LimitOffsetPagination()
                orders = pagination.paginate_queryset(orders, request)
            if not orders:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_orders = OrderSerializer(orders, many=True)
            return Response(data=serialized_orders.data, status=HTTP_200_OK)
            # return Response(data={"count": count, "data": serialized_orders.data}, status=HTTP_200_OK)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_order(cls, request):
        try:
            serialized_order = OrderSerializer(data=request.data)
            if serialized_order.is_valid():
                serialized_order.save()
                return Response(data=serialized_order.data, status=HTTP_201_CREATED)
            return Response(data=serialized_order.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def update_order(cls, request, tracking_number=None):
        try:
            order = Order.objects.filter(tracking_number__iexact=tracking_number, status=Status.ACTIVE).first()
            if not order:
                return Response(data=None, status=HTTP_200_OK)
            serialized_order = OrderSerializer(order, data=request.data, partial=True)
            if serialized_order.is_valid():
                order = serialized_order.save()

                # check if order status is updated
                check_order_status_update(request, order)

                return Response(data=serialized_order.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_order(cls, request, tracking_number=None):
        try:
            Order.objects.filter(tracking_number__iexact=tracking_number).update(status=Status.DELETED)
            return Response(data=None, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)
