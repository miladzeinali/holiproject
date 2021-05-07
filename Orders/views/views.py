from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from Orders.models import *
from Products.models.origin import Product
from Orders.serializers import *
from rest_framework.permissions import AllowAny
from Accounts.models import Userprofile

class Ordermanagements(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    @action(methods=['POST'], detail=False)
    def OrderControl(self, request):
        user = request.user
        data = request.data
        code = data['code']
        qty = data['qty']
        try:
            order = Order.objects.get(user=user, status='Wpay')
            product = Product.objects.get(code=code)
            if product.count != 0 and product.count >= qty:
                price = product.price
                if product.Sale == True:
                    price = product.sale_price
                try:
                    orderitem = OrderItem.objects.get(order=order, product=product)
                    orderitem.quantity += qty
                    orderitem.save()
                except:
                    orderitem.objects.create(order=order, product=product,
                                             quantity=qty, price=price)
                resp = ('product Added',)
                return Response(resp, status=status.HTTP_200_OK)
            else:
                resp = ('product sold Out',)
                return Response(resp, status=status.HTTP_404_NOT_FOUND)
        except:
            order = Order.objects.create(user=user, status='Wpay')
            product = Product.objects.get(code=code)
            if product.count != 0 and product.count >= qty:
                OrderItem.objects.create(order=order, product=product, quantity=qty)
                return Response(('product Added!',), status=status.HTTP_200_OK)
            else:
                order.delete()
                return Response(('product sold Out',), status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=False)
    def OrderItemChange(self,request):
        user=request.user
        code=request.data['code']
        qty=request.data['qty']
        try:
            order=Order.objects.get(user=user,status='Wpay')
            product=Product.objects.get(code=code)
            orderitem=OrderItem.objects.get(order=order,product=product)
            if orderitem.quantity == 1 and qty < 1:
                orderitem.delete()
                order.delete()
                product.save()
                return Response({'product deleted'},status=status.HTTP_200_OK)
            orderitem.quantity += qty
            orderitem.save()
            product.count += -(qty)
            product.save()
            return Response({'OrderItem modified'},status=status.HTTP_200_OK)
        except:
            return Response({'error in modifing Order Item'},status=status.HTTP_304_NOT_MODIFIED)

    @action(methods=['POST'],detail=False)
    def OrderItemDelete(self,request):
        user=request.user
        code=request.data['code']
        try:
            order = Order.objects.get(user=user, status='Wpay')
            product = Product.objects.get(code=code)
            orderitem = OrderItem.objects.get(order=order, product=product)
            orderitem.delete()
            product.count += orderitem.quantity
            return Response({'OrderItem Deleted'},status=status.HTTP_200_OK)
        except:
            return Response({'error in OrderItem Deleting'},status=status.HTTP_304_NOT_MODIFIED)
