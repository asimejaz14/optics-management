from django.shortcuts import render
from rest_framework.permissions import AllowAny

# Create your views here.
from rest_framework.views import APIView

from order.order_controller import OrderController


class OrderView(APIView):
    order_controller = OrderController
    permission_classes = [AllowAny]

    def get(self, request, tracking_number=None):
        return self.order_controller.get_order(request, tracking_number)

    def post(self, request):
        return self.order_controller.create_order(request)

    def patch(self, request, tracking_number=None):
        return self.order_controller.update_order(request, tracking_number)

    def delete(self, request, tracking_number=None):
        return self.order_controller.delete_order(request, tracking_number)


class DashboardView(APIView):
    order_controller = OrderController
    permission_classes = [AllowAny]

    def get(self, request):
        return self.order_controller.get_dashboard(request)
