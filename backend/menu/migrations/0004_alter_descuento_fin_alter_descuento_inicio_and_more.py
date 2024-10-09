# Generated by Django 5.1.1 on 2024-10-08 06:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_descuento_productos_descuento_frecuencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 0, 8, 18, 974011)),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 0, 8, 18, 974011)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descuento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos', to='menu.descuento'),
        ),
    ]