from rest_framework import serializers
from .models import *


class UserprofileSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

