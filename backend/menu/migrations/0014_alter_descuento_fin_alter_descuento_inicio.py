# Generated by Django 5.1.1 on 2024-11-29 02:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_alter_descuento_fin_alter_descuento_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 28, 20, 24, 44, 444290)),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 28, 20, 24, 44, 444290)),
        ),
    ]
