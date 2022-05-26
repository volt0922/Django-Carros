# Generated by Django 3.2.10 on 2022-05-09 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceId', models.CharField(default=0, max_length=255)),
                ('fechaInvoice', models.CharField(default=0, max_length=255)),
                ('cuentaInvoice', models.IntegerField(default=0)),
                ('cantidadInvoice', models.CharField(default=0, max_length=255)),
                ('statusInvoice', models.CharField(default=0, max_length=255)),
                ('fecha_registro', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
