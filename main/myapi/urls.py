from django.urls import path
from django import views
from .views import *


app_name = 'myapi'
urlpatterns = [
    path('', Message, name="message"),
    path('data/<str:pk>', GetBankdetailApiView.as_view(), name="bankdetail")
]