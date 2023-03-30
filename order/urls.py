from django.urls import path

from order import views
urlpatterns = [
    path('', views.OrderView.as_view(), name="Order View"),
    path('dashboard', views.DashboardView.as_view(), name="Dashboard View"),
    path('<str:tracking_number>', views.OrderView.as_view(), name="Order View"),

]

