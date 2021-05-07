from rest_framework import viewsets,status
from ..models.origin import Product
from ..serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import ProductSerializers
from Orders.serializers import *


class homeapis(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    # search_fields =('count','count_sell','price','color')
    search_fields =('title', 'code', 'brand',)           
    def get_serializer_class(self):
        if self.action == 'retrieve' :
            return ProductSerializers
        return ProductSerializers

    @action(methods=['GET'],detail=False)
    def saleproducts(self,request):
        try:
            products = Product.objects.filter(sale=True)
            serializer=ProductSerializers(products,many=True)
            if len(products)==0:
                return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            resp=('fail')
            return Response(resp,status=status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'],detail=False)
    def newestproducts(self,request):
        try:
            products = Product.objects.all().order_by('-date_created')
            serializer=ProductSerializers(products,many=True)
            if len(products)==0:
                return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            resp = ('fail')
            return Response(resp, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'],detail=False)
    def highestcountsell(self,request):
        queryset = Product.objects.all()
        def get_serializer_class(self):
            if self.action == 'retrieve':
                return ProductSerializers
            return ProductSerializers
        try:
            products=Product.objects.all().order_by('-count_sell')[0:4]
            serializer = ProductSerializers(products, many=True)
            if len(products) == 0:
                return Response(serializer.data, status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            resp = ('fail',)
            return Response(resp,status= status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'],detail=False)
    def getorders(self,request):
        user=request.user
        try:
            orderobj=Order.objects.get(user=user,status='Processing')
            orderitemsobj=OrderItem.objects.filter(order=orderobj)
            order=OrderSerializers(order,many=True).data
            orderitems=OrderItemsSerializers(orderitemsobj,many=True)
            resp=(order,orderitems)
            return Response(resp,status=status.HTTP_200_OK)
        except:
            resp=('fail')
            return Response(resp,status=status.HTTP_404_NOT_FOUND)







