# Generated by Django 3.2.7 on 2021-10-03 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('kilojoules', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('sodium', models.FloatField(default=0)),
                ('sugar', models.FloatField(default=0)),
            ],
        ),
    ]