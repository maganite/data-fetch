from rest_framework import serializers
from .models import *

class GetBankdetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank_branches
        fields = '__all__'