# Generated by Django 5.1.1 on 2024-11-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_descuento_fin_alter_descuento_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_Tipo_Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimo', models.IntegerField()),
                ('maximo', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Producto_Tipo_Ingrediente',
                'verbose_name_plural': 'Productos_Tipos_Ingredientes',
                'db_table': 'productos_tipos_ingredientes',
            },
        ),
    ]