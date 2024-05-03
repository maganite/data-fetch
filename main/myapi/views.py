from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import GetBankdetailSerializers
from django.http import HttpResponse

class GetBankdetailApiView(generics.ListAPIView):
    serializer_class = GetBankdetailSerializers

    def get_queryset(self):
        bankbranch = self.kwargs['pk']
        return BankDetail.objects.filter(bank_branch__icontains=bankbranch)
    
