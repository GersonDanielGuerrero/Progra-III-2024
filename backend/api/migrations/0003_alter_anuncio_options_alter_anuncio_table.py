# Generated by Django 5.1.1 on 2024-09-23 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_anuncio_categoria_extras_pregunta_frecuente_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anuncio',
            options={'verbose_name': 'Anuncio', 'verbose_name_plural': 'Anuncios'},
        ),
        migrations.AlterModelTable(
            name='anuncio',
            table='anuncios',
        ),
    ]
