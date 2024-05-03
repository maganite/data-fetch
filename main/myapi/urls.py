from django.urls import path
from .views import *


app_name = 'myapi'
urlpatterns = [
    path('<str:pk>', GetBankdetailApiView.as_view(), name="bankdetail"),
]