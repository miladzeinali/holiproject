from Zarinpal.serializers import *
from django.http import HttpResponse
from zeep import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

MERCHANT = 'fe55ad50-cdb2-11ea-96ef-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
CallbackURL = 'http://127.0.0.1:4200/dashboard/' # Important: need to edit for realy server.

@api_view(['POST'])
def send_request(request):
    data = request.data
    amount = data['totalprice']
    mobile = data['mobile']
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        serializer = ResultSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return HttpResponse('Error code: ' + str(result.Status))

@api_view(['POST'])
def verify(request):
    data = request.data
    if data['Status']=='OK':
        result = client.service.PaymentVerification(MERCHANT,data['Authority'], data['amount'])
        serializer = ResSerializer(result)
        if result.Status == 100:
            return Response(serializer.data,status.HTTP_200_OK)
        elif result.Status == 101:
            return Response(serializer.data,status.HTTP_200_OK)
    else:
        return Response({'resp':'erorr'},status.HTTP_400_BAD_REQUEST)
