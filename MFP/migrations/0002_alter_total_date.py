# Generated by Django 3.2.7 on 2021-10-03 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MFP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='date',
            field=models.DateField(default=datetime.date.today, unique=True),
        ),
    ]
