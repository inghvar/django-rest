from django.urls import path
from .views import ListOrdersView, OrderDetailView


urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('orders/<pk>/', OrderDetailView.as_view(), name="order")
]
