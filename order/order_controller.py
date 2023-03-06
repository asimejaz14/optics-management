from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from order.models import Order
from order.serializers import OrderSerializer


class OrderController:

    @classmethod
    def get_order(cls, request, id=None):

        if id:
            ...
        Order.objects.filter()

        ...

    @classmethod
    def create_order(cls, request):
        serialized_order = OrderSerializer(data=request.data)
        # if serialized_order.is_valid(raise_exception=True):
        if serialized_order.is_valid():
            serialized_order.save()
            return Response(data=serialized_order.data, status=HTTP_201_CREATED)
        return Response(data=serialized_order.errors, status=HTTP_400_BAD_REQUEST)
