from rest_framework import serializers
from .models import *

class GetBankdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = '__all__'