from rest_framework import viewsets,status
from Products.models.MobileVsTablets import Mobile
from Products.serializers import *
from rest_framework.response import Response

class Mobileviewset(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Tabletviewset(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletsSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Headsetsviewset(viewsets.ModelViewSet):
    queryset = Headset.objects.all()
    serializer_class = HeadsetsSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Powerbankviewset(viewsets.ModelViewSet):
    queryset = PowerBank.objects.all()
    serializer_class = PowerbankSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class ChrgerAdabterviewset(viewsets.ModelViewSet):
    queryset = ChargerAdabter.objects.all()
    serializer_class = ChargerAdabterSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Flashmemoryviewset(viewsets.ModelViewSet):
    queryset = FlashMemory.objects.all()
    serializer_class = FlashmemorySerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class mouseviewset(viewsets.ModelViewSet):
    queryset = mouse.objects.all()
    serializer_class = mouseSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class BluetoothDongleviewset(viewsets.ModelViewSet):
    queryset = BluetoothDongle.objects.all()
    serializer_class = BluetoothDongleSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class MobileCoversviewset(viewsets.ModelViewSet):
    queryset = MobileCovers.objects.all()
    serializer_class = MobileCoversSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class ScreenGlassviewset(viewsets.ModelViewSet):
    queryset = ScreenGlass.objects.all()
    serializer_class = ScreenGlassSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class SmartWatchviewset(viewsets.ModelViewSet):
    queryset = SmartWatch.objects.all()
    serializer_class = SmartwatchSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class SDCardsviewset(viewsets.ModelViewSet):
    queryset = SDCards.objects.all()
    serializer_class = SDCardsSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class MonopadVsHoldersviewset(viewsets.ModelViewSet):
    queryset = MonopadVsHolder.objects.all()
    serializer_class = MonopodVsHoldersSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class TVviewset(viewsets.ModelViewSet):
    queryset = TV.objects.all()
    serializer_class = TVSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class CarPlayerviewset(viewsets.ModelViewSet):
    queryset = CarPlayer.objects.all()
    serializer_class = CarPlayerSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Amplifireviewset(viewsets.ModelViewSet):
    queryset = Amplifire.objects.all()
    serializer_class = AmplifireSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')

class Speakerviewset(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializers
    search_fields =('count','count_sell','price','color__color','brand__Brand','title')



