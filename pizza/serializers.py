from rest_framework import serializers
from .models import Order

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pizza', 'customer_name', 'customer_address')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pizza', 'customer_name', 'customer_address')
