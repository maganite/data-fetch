from django.db import models

class BankDetail(models.Model):
    bank_id = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    bank_ifsc = models.CharField(primary_key=True, max_length=11)
    bank_branch = models.CharField(max_length=80)
    bank_address = models.CharField(max_length=200, default='Unknown Address')
    bank_city = models.CharField(max_length=50)
    bank_district = models.CharField(max_length=50)
    bank_state = models.CharField(max_length=26)

    def __str__(self):
        return f"{self.bank_name}--{self.bank_ifsc}"