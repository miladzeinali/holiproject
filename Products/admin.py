from django.contrib import admin
from .models.origin import *
from .models.Accessoris import *
from .models.MobileVsTablets import *
from .models.SoundVsMedia import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category',)
    search_fields = ('Category',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','Brand')
    search_fields = ('id','Brand')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','color')
    search_fields = ('id','color')

class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ('id','guarantee')
    search_fields = ('id','guarantee')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','code','count','count_sell')
    search_fields = ('brand','code')

class SellersAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    search_fields = ('id','user')

class HeadsetAdmin(admin.ModelAdmin):
    list_display = ('id','title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class PowerBankAdmin(admin.ModelAdmin):
    list_display = ('id','title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class ChargerAdapterAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class FlashMemoryAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class mouseAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class BluetoothDongleAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class MobileCoversAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class ScreenGlassAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class SmartWatchAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class SDCardsAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class MonopodVsHolderAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class MobileAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class TabletsAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class TVAAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class CarPlayerAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class AmplifireAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('title','owner','CountSell','code','count')
    search_fields = ('id','title','owner','CountSell','code','count')



admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Guarantee,GuaranteeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Sellers,SellersAdmin)
admin.site.register(Headset,HeadsetAdmin)
admin.site.register(PowerBank,PowerBankAdmin)
admin.site.register(ChargerAdabter,ChargerAdapterAdmin)
admin.site.register(FlashMemory,FlashMemoryAdmin)
admin.site.register(mouse,mouseAdmin)
admin.site.register(BluetoothDongle,BluetoothDongleAdmin)
admin.site.register(MobileCovers,MobileCoversAdmin)
admin.site.register(ScreenGlass,ScreenGlassAdmin)
admin.site.register(SmartWatch,SmartWatchAdmin)
admin.site.register(SDCards,SDCardsAdmin)
admin.site.register(MonopadVsHolder,MonopodVsHolderAdmin)
admin.site.register(Mobile,MobileAdmin)
admin.site.register(Tablet,TabletsAdmin)
admin.site.register(TV,TVAAdmin)
admin.site.register(CarPlayer,CarPlayerAdmin)
admin.site.register(Amplifire,AmplifireAdmin)
admin.site.register(Speaker,SpeakerAdmin)





