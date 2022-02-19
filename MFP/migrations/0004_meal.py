# Generated by Django 3.2.7 on 2021-10-03 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MFP', '0003_auto_20211003_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('type', models.TextField()),
                ('kilojoules', models.FloatField(default=0)),
                ('carbohydrates', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('sodium', models.FloatField(default=0)),
                ('sugar', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
