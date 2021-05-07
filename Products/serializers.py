from rest_framework import serializers
from .models.origin import *
from .models.SoundVsMedia import *
from .models.MobileVsTablets import *
from .models.Accessoris import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    class Meta:
        model = Product
        fields = '__all__'

class ownerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = ('id','user','shop_name')

class GuarranteeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guarantee
        fields = '__all__'

class HeadsetsSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Headset
        fields = '__all__'

class PowerbankSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = PowerBank
        fields = '__all__'

class ChargerAdabterSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    # guarantee = GuaranteeSerializers()
    # owner = ownerSerializers()
    class Meta:
        model = ChargerAdabter
        fields = '__all__'

class FlashmemorySerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = FlashMemory
        fields = '__all__'

class mouseSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = mouse
        fields = '__all__'

class BluetoothDongleSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = BluetoothDongle
        fields = '__all__'

class MobileCoversSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = MobileCovers
        fields = '__all__'

class ScreenGlassSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = ScreenGlass
        fields = '__all__'

class SmartwatchSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = SmartWatch
        fields = '__all__'

class SDCardsSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = SDCards
        fields = '__all__'

class MonopodVsHoldersSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = MonopadVsHolder
        fields = '__all__'

class ElectricConverterSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = ElectricConverter
        fields = '__all__'

class CameraGlassSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = CameraGlass
        fields = '__all__'

class ModemSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Modem
        fields = '__all__'

class MobileBatterySerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = MobileBattery
        fields = '__all__'

class MobileSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    brand = BrandSerializers()
    color = ColorSerializers()
    class Meta:
        model = Mobile
        fields = '__all__'

class AuxCableSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = AuxCable
        fields = '__all__'

class ConverterSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Converter
        fields = '__all__'

class HcoversSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Hcovers
        fields = '__all__'

class TabletsSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Tablet
        fields = '__all__'

class TVSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = TV
        fields = '__all__'

class CarPlayerSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = CarPlayer
        fields = '__all__'

class AmplifireSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Amplifire
        fields = '__all__'

class SpeakerSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    color = ColorSerializers()
    category = CategorySerializers()
    guarantee = GuarranteeSerializers()
    owner = ownerSerializers()
    class Meta:
        model = Speaker
        fields = "__all__"