from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from ..serializers import *
from Orders.models import OrderManagement
from Accounts.models import Userprofile
from Accounts.SmsHandler import SmsHandler
import random
sms = SmsHandler()

class OrderProgress(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    search_fields =('status','province','city','created')

    @action(methods=['GET'],detail=False)
    def CartItems(self,request):
        try:
            user = request.user
            order = Order.objects.get(user=user,status='Wpay')
            orderitems = OrderItem.objects.filter(order=order)
            orderitemslist=[]
            SoldOutProduct=0
            for orderitem in orderitems:
                if orderitem.product.count >= orderitem.quantity:
                    orderitemslist.append(orderitem)
                else:
                    SoldOutProduct +=1
            serializer = OrderItemsSerializers(orderitemslist,many=True)
            return Response(serializer.data,status.HTTP_200_OK)
        except:
            user=request.user
            return Response({'resp':f'can not found an order or orderitems for user{user}'})

    @action(methods=['GET'],detail=False)
    def OrderConfirmPrice(self,request):
        try:
            user=request.user
            order=Order.objects.get(user=user,status='Wpay')
            orderitems=OrderItem.objects.filter(order=order)
            OffPrice = 0
            TotalPrice = 0
            for orderitem in orderitems:
                if orderitem.product.Sale == True:
                    TotalPrice += orderitem.product.sale_price*orderitem.quantity
                    OffPrice += (orderitem.product.price-orderitem.product.sale_price)*orderitem.quantity
                    orderitem.price = orderitem.product.sale_price
                    orderitem.save()
                else:
                    orderitem.price = orderitem.product.price
                    orderitem.save()
                    TotalPrice += orderitem.product.price*orderitem.quantity
            try:
                OffPercent = OffPrice / TotalPrice
            except:
                OffPercent = 0
            SendCost = 40000
            r = {
                "offprice":OffPrice,
                "totalprice":TotalPrice,
                "offpercent":OffPercent,
                "sendcost":SendCost,
                "count":len(orderitems) # قلم کالا
            }
            return Response(r,status=status.HTTP_200_OK)
        except:
            return Response(('erorr in calculate price',),status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def OrderToPay(self, request):
        user = request.user
        try:
            data = request.data
            offprice = data['offprice']
            totalprice = data['totalprice']
            offpercent = data['offpercent']
            sendcost = data['sendcost']
            count = data['count']
        except:
            return Response({'resp': 'detials for pay not founded'}, status.HTTP_404_NOT_FOUND)
        try:
            order = Order.objects.get(user=user, status='Wpay')
            address = Address.objects.get(user=user)
            mobile = Userprofile.objects.get(user=user).mobile
            code = f"{user.id}{order.id}{address.id}{mobile}"
            try:
                OrderManagement.objects.get(order=order, status='Wpay')
            except:
                OrderManagement.objects.create(status='Wpay', user=user, province=address.province,
                                               first_name=address.first_name,
                                               last_name=address.last_name, city=address.city,
                                               district=address.district,
                                               order=order, totalprice=totalprice, mobile=mobile, sendcost=sendcost,
                                               count=count, offpercent=offpercent, offprice=offprice, code=code)
            r = {
                'status': 'success',
                'totalprice': totalprice,
                'mobile': mobile,
            }
            return Response(r, status.HTTP_200_OK)
        except:
            return Response({'resp': 'can not create order management object'}, status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def orderpayed(self, request):
        try:
            user = request.user
            order = Order.objects.get(user=user, status='Wpay')
            ordermanage = OrderManagement.objects.get(order=order, status='Wpay')
            ordermanage.status = 'Processing'
            order.status = 'Processing'
            randnum = random.randint(100, 999)
            code = f"{order.id}{ordermanage.id}{ordermanage.mobile}{randnum}"
            order.code = code
            ordermanage.code = code
            ordermanage.save()
            order.save()
            Transaction.objects.create(first_user=user, type='ci', price=ordermanage.totalprice,
                                       code=code, description='order payed')
            orderitems = OrderItem.objects.filter(order=order)
            for orderitem in orderitems:
                ddd = orderitem.product
                ddd.count -= orderitem.quantity
                ddd.count_sell += orderitem.quantity
                ddd.save()
                userowner = orderitem.product.owner.user
                profile = Userprofile.objects.get(user=userowner)
                profile.credit += orderitem.price
                profile.save()
                Transaction.objects.create(first_user=user, second_user=userowner, price=orderitem.price,
                                           type='tr', code=code,
                                           description=f'{orderitem.id}{code}')
            token = sms.get_token()
            resp = sms.send_order_code(str(code), ordermanage.mobile, token)
            return Response(resp, status.HTTP_200_OK)
        except:
            return Response({'resp': 'erorr in orderpayed process'}, status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET','POST'],detail=False)
    def reportadmin(self,request):
        try:
            if request.method == 'POST':
                try:
                    data = request.data
                    code = data['code']
                    order = OrderManagement.objects.get(code=code)
                    order.status = 'Sended'
                    order.save()
                    mobile = order.mobile
                    token = sms.get_token()
                    resp = sms.send_order_code(code,str(mobile),token)
                    return Response(resp,status.HTTP_200_OK)
                except:
                    return Response({'resp':'erorr in changing status and sms'},status.HTTP_400_BAD_REQUEST)
            elif request.method == 'GET':
                try:
                    order = OrderManagement.objects.filter(status='Processing')
                    serializer = OrdermanagementSerializers(order,many=True)
                    return Response(serializer.data,status.HTTP_200_OK)
                except:
                    return Response({'resp':'Fuck this Ordermanagment serializer and Bye'},status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'resp':'erorr in methods'},status.HTTP_400_BAD_REQUEST)
