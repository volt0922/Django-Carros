# Generated by Django 3.2.10 on 2022-02-25 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_inventory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]