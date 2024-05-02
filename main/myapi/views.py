from django.shortcuts import render
from main.settings import BASE_DIR
from rest_framework import generics
from rest_framework.response import Response
from django.db import IntegrityError
from .models import *
import pandas as pd
from django.http import HttpResponse

def Message(request):
    file_path = BASE_DIR / 'bank_branches.csv'
    df = pd.read_csv(file_path, delimiter=',')
    check=0
    print(df.columns)

    # for i in range(len(df)):
    #     try:
    #         Bank_branches.objects.create(
    #             Bank_id = df.values[i][1],
    #             Bank_name = df.values[i][7],
    #             Bank_ifsc = df.values[i][0],
    #             Bank_branch = df.values[i][2],
    #             Bank_address = df.values[i][3],
    #             Bank_city = df.values[i][4],
    #             Bank_district = df.values[i][5],
    #             Bank_state = df.values[i][6],
    #         )
    #     except IntegrityError:
    #         check=1
    
    # if check==1:
    #     val = "<h1>DATA ALREADY EXISTS! Pass the Bank Branch to get details</h1>"
    #     return HttpResponse(val)
    
    return HttpResponse("<h1>DATA CREATED SUCCESSFULLY! Pass the Bank Branch to get details")

    
class GetBankdetailApiView(generics.ListCreateAPIView):
    pass
