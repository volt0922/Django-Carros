# Generated by Django 3.2.10 on 2022-03-28 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parte', '0010_auto_20220131_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parte',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='parte',
            name='descuentoTotal',
        ),
        migrations.RemoveField(
            model_name='parte',
            name='resumen',
        ),
        migrations.RemoveField(
            model_name='parte',
            name='total',
        ),
    ]