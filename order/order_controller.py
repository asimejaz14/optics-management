from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED

from common.enums import Status
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
            orders = Order.objects.filter(status=Status.ACTIVE)
            if not orders:
                return Response(data=None, status=HTTP_204_NO_CONTENT)
            serialized_orders = OrderSerializer(orders, many=True)
            return Response(data=serialized_orders.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def create_order(cls, request):
        try:
            print("1")
            serialized_order = OrderSerializer(data=request.data)
            print("2")
            if serialized_order.is_valid():
                print("3")
                serialized_order.save()
                print("4")
                return Response(data=serialized_order.data, status=HTTP_201_CREATED)
            return Response(data=serialized_order.errors, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def updated_order(cls, request):
        try:
            ...
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete_order(cls, request, tracking_number=None):
        try:
            Order.objects.filter(tracking_number__iexact=tracking_number).update(status=Status.DELETED)
            return Response(data=None, status=HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(data=e, status=HTTP_500_INTERNAL_SERVER_ERROR)
