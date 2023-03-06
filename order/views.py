from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from order.order_controller import OrderController


class OrderView(APIView):
    order_controller = OrderController

    def get(self, request, id=None):
        return self.order_controller.get_order(request, id)

    def post(self, request):
        return self.order_controller.create_order(request)
