from django.core.management.base import BaseCommand
from main.settings import BASE_DIR
import pandas as pd
from myapi.models import BankDetail
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Saving the database'

    def handle(self, *args, **kwargs):
        file_path = BASE_DIR / 'bank_branches.csv'
        df = pd.read_csv(file_path, delimiter=',')

        instances = []
        check = False

        for _, row in df.iterrows():
            instance = BankDetail(
                bank_ifsc=row['bank_ifsc'],
                bank_id=row['bank_id'],
                bank_branch=row['bank_branch'],
                bank_address=row['bank_address'],
                bank_city=row['bank_city'],
                bank_district=row['bank_district'],
                bank_state=row['bank_state'],
                bank_name=row['bank_name']
            )
            instances.append(instance)

        try:
            BankDetail.objects.bulk_create(instances)
        except IntegrityError:
            check = True

        if check == True:
            self.stdout.write("Data already present")