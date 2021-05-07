from rest_framework import viewsets,status
from ..models.origin import Product
from ..models.MobileVsTablets import *
from ..models.Accessoris import *
from ..models.SoundVsMedia import *
from ..serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DetailProducts(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # permission_classes = (IsAuthenticated,)

    @action(methods=['GET','POST'],detail=False)
    def detailpro(self,request):
        try:
            data=request.data
            code=data['code']
            if code.startswith('mob'):
                product=Mobile.objects.get(code=code)
                serializer=MobileSerializers(product)
                return Response(serializer.data,status.HTTP_200_OK)
            elif code.startswith('tab'):
                product = Tablet.objects.get(code=code)
                serializer = TabletsSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('hea'):
                product = Headset.objects.get(code=code)
                serializer = HeadsetsSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('pow'):
                product = PowerBank.objects.get(code=code)
                serializer = PowerbankSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('cha'):
                product = ChargerAdabter.objects.get(code=code)
                serializer = ChargerAdabterSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('fla'):
                product = FlashMemory.objects.get(code=code)
                serializer = FlashmemorySerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('mou'):
                product = mouse.objects.get(code=code)
                serializer = mouseSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('blu'):
                product = BluetoothDongle.objects.get(code=code)
                serializer = BluetoothDongleSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('moco'):
                product = MobileCovers.objects.get(code=code)
                serializer = MobileCoversSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('scgl'):
                product = ScreenGlass.objects.get(code=code)
                serializer = ScreenGlassSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('smwa'):
                product = SmartWatch.objects.get(code=code)
                serializer = SmartwatchSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('sdca'):
                product = SDCards.objects.get(code=code)
                serializer = SDCardsSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('mono'):
                product = MonopadVsHolder.objects.get(code=code)
                serializer = MonopodVsHoldersSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('elco'):
                product = ElectricConverter.objects.get(code=code)
                serializer = ElectricConverterSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('cagl'):
                product = CameraGlass.objects.get(code=code)
                serializer = CameraGlassSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('mod'):
                product = Modem.objects.get(code=code)
                serializer = ModemSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('mobat'):
                product = MobileBattery.objects.get(code=code)
                serializer = MobileBatterySerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('aux'):
                product = AuxCable.objects.get(code=code)
                serializer = AuxCableSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('conv'):
                product = Converter.objects.get(code=code)
                serializer = ConverterSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('hco'):
                product = Hcovers.objects.get(code=code)
                serializer = HcoversSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('tv'):
                product = TV.objects.get(code=code)
                serializer = TVSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('capl'):
                product = CarPlayer.objects.get(code=code)
                serializer = CarPlayerSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('amp'):
                product = Amplifire.objects.get(code=code)
                serializer = AmplifireSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
            elif code.startswith('spe'):
                product = Speaker.objects.get(code=code)
                serializer = SpeakerSerializers(product)
                return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'erorr in product detail'},status=status.HTTP_400_BAD_REQUEST)
