from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login,logout,authenticate
from .serializers import *
import random
from rest_framework.authtoken.models import Token
from Accounts.SmsHandler import SmsHandler
import datetime
from Orders.models import OrderManagement
from Orders.serializers import OrdermanagementSerializers
sms=SmsHandler()

class Usermanagement(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers

    @action(methods=['POST'],detail=False)
    def getphone(self,request):
        data = request.data
        mobile=data['mobile']
        try:
            Userprofile.objects.get(mobile=mobile)
            resp = ('User registered before!',)
            return Response(resp,status.HTTP_400_BAD_REQUEST)
        except:
            pass
        try:
            num=random.randint(1000,9999)
            ValidationCode.objects.create(mobile=mobile,validation_code=num,time_created=datetime.datetime.now())
            token=sms.get_token()
            resp=sms.send_register_code(code=str(num),mobile=mobile,token=token)
            return Response(resp,status.HTTP_201_CREATED)
        except:
            return Response(('erorr in send validiation code',),status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def userverify(self,request):
        data = request.data
        mobile=data['mobile']
        code=data['code']
        try:
            obj=ValidationCode.objects.get(mobile=mobile,validation_code=code)
            obj.delete()
            user=User.objects.create(username=mobile,password=code,last_login=datetime.datetime.now())
            Userprofile.objects.create(mobile=mobile,type=1,user=user)
            token = Token.objects.create(user=user)
            return Response({'token':token.key,'resp':'Verifying user and Register seccessfull and user logged in!'},status.HTTP_200_OK)
        except:
            pass
        try:
            ValidationCode.objects.get(mobile=mobile)
            return Response(('incorrect password',),status.HTTP_400_BAD_REQUEST)
        except:
            return Response(('erorr in userverify',),status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def login(self,request):
        data=request.data
        try:
            mobile = data['username']
            password = data['password']
            try:
                user = Userprofile.objects.get(mobile=mobile).user
                userlogin=authenticate(request,username=mobile,password=password)
                if userlogin is not None:
                    try:
                        token = Token.objects.get(user=user)
                        user.last_login = datetime.datetime.now()
                        user.save()
                        print(token)
                        return Response({'token':token.key,'resp':f'user logged in {mobile}'},status.HTTP_200_OK)
                    except:
                        return Response({'resp':f'token not found for {mobile}'},status.HTTP_400_BAD_REQUEST)
                else:
                    return Response((f'incorrect password {mobile}',),status.HTTP_400_BAD_REQUEST)
            except:
                return Response(('User not found!'),status.HTTP_404_NOT_FOUND)
        except:
            return Response(('data not found from post method'),status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def logout(self,request):
        try:
            user=request.user
            logout(request)
            return Response((f'user logged out {user}',),status.HTTP_200_OK)
        except:
            return Response((f'error in login out {user}',),status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def forgetpass(self,request):
        data=request.data
        mobile=data['mobile']
        try:
            Userprofile.objects.get(mobile=mobile)
            num = random.randint(1000,9999)
            ValidationCode.objects.create(mobile=mobile,validation_code=num,time_created=datetime.datetime.now())
            token = sms.get_token()
            resp = sms.send_forget_code(str(num),mobile,token)
            return Response(resp,status.HTTP_201_OK)
        except:
            return Response(('user not found',),status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'],detail=False)
    def setnewpass(self,request):
        try:
            data = request.data
            mobile = data['mobile']
            code = data['code']
            try:
                validcode = ValidationCode.objects.get(mobile=mobile,validation_code=code)
                user = Userprofile.objects.get(mobile=mobile).user
                user.set_password(code)
                user.save()
                token = Token.objects.get(user=user)
                validcode.delete()
                return Response({"token":token,"resp":'pass changed'},status.HTTP_200_OK)
            except:
                pass
            try:
                ValidationCode.objects.get(mobile=mobile)
                return Response(('incorrect pass',),status.HTTP_400_BAD_REQUEST)
            except:
                return Response(('erorr in changing pass',),status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'resp':'erorr in set new pass'},status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'],detail=False)
    def AddressCreate(self,request):
        user=request.user
        data=request.data
        try:
            Address.objects.get(user=user)
            return Response(('address created before',),status.HTTP_400_BAD_REQUEST)
        except:
            Address.objects.create(user=user,province=data['province'],
            city=data['city'],district=data['district'],
            postcode=data['postcode'],first_name=data['first_name'],last_name=data['last_name'])
            return Response(('address created',),status.HTTP_200_OK)

    @action(methods=['PUT'],detail=False)
    def AddressChange(self,request):
        user=request.user
        data=request.data
        try:
            address=Address.objects.get(user=user)
            provice=data['province']
            city=data['city']
            district=data['district']
            postcode = data['postcode']
            first_name=data['first_name']
            last_name=data['last_name']
            address.province=provice
            address.city=city
            address.district=district
            address.postcode = postcode
            address.last_name=last_name
            address.first_name =first_name
            address.save()
            return Response(('address modified',),status=status.HTTP_200_OK)
        except:
            return Response(('erorr in address modifing',),status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'],detail=False)
    def AddressDelete(self,request):
        user=request.user
        try:
            address=Address.objects.get(user=user)
            address.delete()
            return Response(('address deleted',),status.HTTP_200_OK)
        except:
            return Response(('erorr in address deleting',),status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],detail=False)
    def ProcessingOrder(self,request):
        try:
            user = request.user
            Processing = OrderManagement.objects.filter(user=user,status='Processing')
            serializer = OrdermanagementSerializers(Processing,many=True)
            return Response(serializer.data,status.HTTP_200_OK)
        except:
            return Response({'resp':'erorr in filtering ordermanagements'},status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def SendedOrder(self, request):
        try:
            user = request.user
            Sended = OrderManagement.objects.filter(user=user, status='Sended')
            serializer = OrdermanagementSerializers(Sended, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'resp': 'erorr in filtering ordermanagements'}, status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def DeliveredOrder(self, request):
        try:
            user = request.user 
            Delivered = OrderManagement.objects.filter(user=user, status='Delivered')
            serializer = OrdermanagementSerializers(Delivered, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'resp': 'erorr in filtering ordermanagements'}, status.HTTP_400_BAD_REQUEST)




