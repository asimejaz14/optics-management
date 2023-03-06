from django.urls import path

from order import views

urlpatterns = [
    path('', views.OrderView.as_view(), name="Order View"),
    # path('<string:tracking_number>', views.OrderView.as_view(), name="Order View"),
]
