from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED

from common import enums
from common.enums import Status, OrderStatus, ORDER_SORTING_KEYS
from common.utils import send_message, get_default_query_param
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
            q = get_default_query_param(request, "q", None)
            date = get_default_query_param(request, "date", None)
            order_by = get_default_query_param(request, "order_by", "created_at")
            order = get_default_query_param(request, "order", "desc")
            limit = get_default_query_param(request, "limit", None)
            offset = get_default_query_param(request, "offset", None)
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
                # return Response(data=None, status=HTTP_204_NO_CONTENT)
                return Response(data=[], status=HTTP_200_OK)
            serialized_orders = OrderSerializer(orders, many=True)
            return Response(data={"count": count, "data": serialized_orders.data}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
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

    @classmethod
    def get_dashboard(cls, request):

        data = {
            "total_orders": Order.objects.filter(status=1).count(),
            "created_orders": Order.objects.filter(status=1, order_status=0).count(),
            "in_progress_orders": Order.objects.filter(status=1, order_status=1).count(),
            "ready_orders": Order.objects.filter(status=1, order_status=2).count(),
            "completed_orders": Order.objects.filter(status=1, order_status=3).count()
        }

        return Response(data=data, status=HTTP_200_OK)
