from rest_framework import serializers
from .models import *
from Products.serializers import ProductSerializers

class OrderSerializers(serializers.ModelSerializer):
    get_total_quantity = serializers.IntegerField()
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemsSerializers(serializers.ModelSerializer):
    order= OrderSerializers()
    product = ProductSerializers()
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrdermanagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderManagement
        fields = '__all__'
