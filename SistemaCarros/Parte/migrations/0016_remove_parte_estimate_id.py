# Generated by Django 3.2.10 on 2022-05-05 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parte', '0015_alter_parte_descuento_parte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parte',
            name='estimate_id',
        ),
    ]