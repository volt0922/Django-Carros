# Generated by Django 3.2.10 on 2022-05-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0005_auto_20220513_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestos',
            name='descuentoTotal_manaobra',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presupuestos',
            name='descuentoTotal_parte',
            field=models.FloatField(blank=True, null=True),
        ),
    ]