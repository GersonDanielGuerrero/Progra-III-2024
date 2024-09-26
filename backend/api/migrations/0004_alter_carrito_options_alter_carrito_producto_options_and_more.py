# Generated by Django 5.1.1 on 2024-09-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_anuncio_options_alter_anuncio_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'verbose_name': 'Carrito', 'verbose_name_plural': 'Carritos'},
        ),
        migrations.AlterModelOptions(
            name='carrito_producto',
            options={'verbose_name': 'Carrito_Producto', 'verbose_name_plural': 'Carritos_Productos'},
        ),
        migrations.AlterModelOptions(
            name='carrito_producto_extra',
            options={'verbose_name': 'Carrito_Producto_Extra', 'verbose_name_plural': 'Carritos_Productos_Extras'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='combo_producto',
            options={'verbose_name': 'Combo_Producto', 'verbose_name_plural': 'Combos_Productos'},
        ),
        migrations.AlterModelOptions(
            name='descuento',
            options={'verbose_name': 'Descuento', 'verbose_name_plural': 'Descuentos'},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name': 'Direccion', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AlterModelOptions(
            name='extras',
            options={'verbose_name': 'Extra', 'verbose_name_plural': 'Extras'},
        ),
        migrations.AlterModelOptions(
            name='ingrediente',
            options={'verbose_name': 'Ingrediente', 'verbose_name_plural': 'Ingredientes'},
        ),
        migrations.AlterModelOptions(
            name='mensaje',
            options={'verbose_name': 'Mensaje', 'verbose_name_plural': 'Mensajes'},
        ),
        migrations.AlterModelOptions(
            name='pregunta_frecuente',
            options={'verbose_name': 'Pregunta_Frecuente', 'verbose_name_plural': 'Preguntas_Frecuentes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name': 'Rol', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='tipo_ingrediente',
            options={'verbose_name': 'Tipo_Ingrediente', 'verbose_name_plural': 'Tipos_Ingrediente'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AlterModelOptions(
            name='venta_producto',
            options={'verbose_name': 'Venta_Producto', 'verbose_name_plural': 'Ventas_Productos'},
        ),
        migrations.AlterModelOptions(
            name='venta_producto_extra',
            options={'verbose_name': 'Venta_Producto_Extra', 'verbose_name_plural': 'Ventas_Productos_Extras'},
        ),
        migrations.AlterModelTable(
            name='carrito',
            table='carritos',
        ),
        migrations.AlterModelTable(
            name='carrito_producto',
            table='carritos_productos',
        ),
        migrations.AlterModelTable(
            name='carrito_producto_extra',
            table='carritos_productos_extras',
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='categorias',
        ),
        migrations.AlterModelTable(
            name='combo_producto',
            table='combos_productos',
        ),
        migrations.AlterModelTable(
            name='descuento',
            table='descuentos',
        ),
        migrations.AlterModelTable(
            name='direccion',
            table='direcciones',
        ),
        migrations.AlterModelTable(
            name='extras',
            table='extras',
        ),
        migrations.AlterModelTable(
            name='ingrediente',
            table='ingredientes',
        ),
        migrations.AlterModelTable(
            name='mensaje',
            table='mensajes',
        ),
        migrations.AlterModelTable(
            name='pregunta_frecuente',
            table='preguntas_frecuentes',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='productos',
        ),
        migrations.AlterModelTable(
            name='rol',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='tipo_ingrediente',
            table='tipo_ingredientes',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuarios',
        ),
        migrations.AlterModelTable(
            name='venta',
            table='ventas',
        ),
        migrations.AlterModelTable(
            name='venta_producto',
            table='ventas_productos',
        ),
        migrations.AlterModelTable(
            name='venta_producto_extra',
            table='ventas_productos_extras',
        ),
    ]