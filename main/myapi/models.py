from django.db import models

class Bank_branches(models.Model):
    Bank_id = models.IntegerField()
    Bank_name = models.CharField(max_length=50)
    Bank_ifsc = models.CharField(primary_key=True, max_length=11)
    Bank_branch = models.CharField(max_length=80)
    Bank_address = models.CharField(max_length=200, default='Unknown Address')
    Bank_city = models.CharField(max_length=50)
    Bank_district = models.CharField(max_length=50)
    Bank_state = models.CharField(max_length=26)

    def __str__(self):
        return f"{self.Bank_name}--{self.Bank_ifsc}"