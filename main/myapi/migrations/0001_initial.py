# Generated by Django 4.2.11 on 2024-05-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_branches',
            fields=[
                ('bank_id', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('bank_branch', models.CharField(max_length=80)),
                ('bank_city', models.CharField(max_length=50)),
                ('bank_district', models.CharField(max_length=50)),
                ('bank_state', models.CharField(max_length=26)),
            ],
        ),
    ]
